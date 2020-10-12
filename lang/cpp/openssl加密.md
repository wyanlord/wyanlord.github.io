### 1、MD5加密

```cpp
#include <cstdio>
#include <cstring>
#include <openssl/md5.h>
#include <cstdlib>

char *md5(const char *src);

int main() {
    char *str = md5("123456");
    printf("%s", str);
    free(str);

    return 0;
}

char *md5(const char *src) {
    char szTmp[3];
    unsigned char c[MD5_DIGEST_LENGTH];
    char *out = (char *) malloc(MD5_DIGEST_LENGTH * 2 + 4);

    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, src, strlen(src));
    MD5_Final(c, &ctx);

    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        sprintf(szTmp, "%02X", c[i]);
        memcpy(&out[i * 2], szTmp, 2);
    }

    return out;
}
```

### 2、SHA1加密

```cpp
#include <cstdio>
#include <cstring>
#include <openssl/sha.h>
#include <cstdlib>

char *sha1(const char *src);

int main() {
    char *str = sha1("123456");
    printf("%s", str);
    free(str);

    return 0;
}

char *sha1(const char *src) {
    char szTmp[3];
    unsigned char c[SHA_DIGEST_LENGTH];
    char *out = (char *) malloc(SHA_DIGEST_LENGTH * 2 + 4);

    SHA_CTX ctx;
    SHA1_Init(&ctx);
    SHA1_Update(&ctx, src, strlen(src));
    SHA1_Final(c, &ctx);

    for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
        sprintf(szTmp, "%02X", c[i]);
        memcpy(&out[i * 2], szTmp, 2);
    }

    return out;
}
```

### 3、SHA512加密

```cpp
#include <cstdio>
#include <cstring>
#include <openssl/sha.h>
#include <cstdlib>

char *sha512(const char *src);

int main() {
    char *str = sha512("123456");
    printf("%s", str);
    free(str);

    return 0;
}

char *sha512(const char *src) {
    char szTmp[3];
    unsigned char c[SHA512_DIGEST_LENGTH];
    char *out = (char *) malloc(SHA512_DIGEST_LENGTH * 2 + 4);

    SHA512_CTX ctx;
    SHA512_Init(&ctx);
    SHA512_Update(&ctx, src, strlen(src));
    SHA512_Final(c, &ctx);

    for (int i = 0; i < SHA512_DIGEST_LENGTH; i++) {
        sprintf(szTmp, "%02X", c[i]);
        memcpy(&out[i * 2], szTmp, 2);
    }

    return out;
}
```

### 4、AES加解密

```cpp
#include <cstdio>
#include <cstring>
#include <openssl/aes.h>
#include <cstdlib>

char * aes_encrypt(const char *in, const char *key);
char * aes_decrypt(const char *in, const char *key);

int main() {
    const char *src = "123456";
    const char *key = "0123456789abcdef";

    char *out_enc = aes_encrypt(src, key);
    printf("encode result = %s\n", out_enc);

    char *out_dec = aes_decrypt(out_enc, key);
    printf("decode result = %s\n", out_dec);

    free(out_enc);
    free(out_dec);

    return 0;
}

char *aes_encrypt(const char *in, const char *key) {
    AES_KEY aes;
    if (AES_set_encrypt_key((unsigned char *) key, 128, &aes) < 0) {
        return NULL;
    }

    int len = strlen(in), padding = AES_BLOCK_SIZE - len % AES_BLOCK_SIZE;

    char inData[len + padding];
    memcpy(inData, in, len);
    for(int i = 0; i < padding; i++) {
        inData[len + i] = padding;
    }

    char *out = (char *) malloc(len + padding + 1);
    memset(out, 0, len + padding + 1);

    for (int j = 0; j < len + padding; j += AES_BLOCK_SIZE) {
        AES_ecb_encrypt((unsigned char *) inData + j, (unsigned char *) out + j, &aes, AES_ENCRYPT);
    }

    return out;
}

char *aes_decrypt(const char *in, const char *key) {
    AES_KEY aes;
    if (AES_set_decrypt_key((unsigned char *) key, 128, &aes) < 0) {
        return NULL;
    }

    int len = strlen(in);
    char *out = (char *) malloc(len + 1);
    memset(out, 0, len + 1);

    for(int j = 0; j < len; j += AES_BLOCK_SIZE) {
        AES_ecb_encrypt((unsigned char *) in + j, (unsigned char *) out + j, &aes, AES_DECRYPT);
    }

    *(out + len - *(out + len - 1)) = '\0';

    return out;
}
```

### 5、base64编解码

```cpp
#include <openssl/evp.h>
#include <openssl/bio.h>
#include <openssl/buffer.h>
#include <cstring>

char *base64_encode(const char *in, int length, bool newLine);
char *base64_decode(const char *in, int length, bool newLine);

int main(int argc, char *argv[]) {
    const char *src = "hello world";

    char *encode = base64_encode(src, strlen(src), false);
    printf("base64 encode: %s\n", encode);

    char *decode = base64_decode(encode, strlen(encode), false);
    printf("base64 decode: %s\n", decode);
    
    free(encode);
    free(decode);
    
    return 0;
}

char *base64_encode(const char *in, int length, bool newLine) {
    BIO *b64 = NULL;
    BUF_MEM *pp = NULL;

    b64 = BIO_new(BIO_f_base64());
    if (!newLine) {
        BIO_set_flags(b64, BIO_FLAGS_BASE64_NO_NL);
    }

    b64 = BIO_push(b64, BIO_new(BIO_s_mem()));
    BIO_write(b64, in, length);
    BIO_flush(b64);
    BIO_get_mem_ptr(b64, &pp);
    BIO_set_close(b64, BIO_NOCLOSE);

    char *buff = (char *) malloc(pp->length + 1);
    memcpy(buff, pp->data, pp->length);
    buff[pp->length] = 0;
    BIO_free_all(b64);

    return buff;
}

char *base64_decode(const char *in, int length, bool newLine) {
    BIO *b64 = NULL;
    BIO *bm = NULL;

    char *buffer = (char *) malloc(length);
    memset(buffer, 0, length);

    b64 = BIO_new(BIO_f_base64());
    if (!newLine) {
        BIO_set_flags(b64, BIO_FLAGS_BASE64_NO_NL);
    }

    bm = BIO_new_mem_buf(in, length);
    bm = BIO_push(b64, bm);
    BIO_read(bm, buffer, length);
    BIO_free_all(bm);

    return buffer;
}
```

### 6、RSA加解密

```cpp
#include <openssl/rsa.h>
#include <openssl/pem.h>
#include <cstring>

void RSA_keys(int key_len, char **pri_key, char **pub_key);

char *RSA_encrypt(const char *pub_key, const char *data);

char *RSA_decrypt(const char *pri_key, const char *data);

int main(int argc, char *argv[]) {
    char *pri_key = NULL;
    char *pub_key = NULL;

    RSA_keys(1024, &pri_key, &pub_key);

    const char *src = "hello";

    char *data_enc = RSA_encrypt(pub_key, src);
    char *data_dec = RSA_decrypt(pri_key, data_enc);

    printf("pri key: %s\npub key: %s\n", pri_key, pub_key);
    printf("data enc: %s\ndata dec: %s\n", data_enc, data_dec);

    free(pri_key);
    free(pub_key);
    free(data_enc);
    free(data_dec);

    return 0;
}

void RSA_keys(int key_len, char **pri_key, char **pub_key) {
    size_t pri_len;
    size_t pub_len;

    RSA *key_pair = RSA_generate_key(key_len, RSA_F4, NULL, NULL);

    BIO *pri = BIO_new(BIO_s_mem());
    BIO *pub = BIO_new(BIO_s_mem());

    PEM_write_bio_RSAPrivateKey(pri, key_pair, NULL, NULL, 0, NULL, NULL);
    PEM_write_bio_RSAPublicKey(pub, key_pair);

    pri_len = BIO_pending(pri);
    pub_len = BIO_pending(pub);

    *pri_key = (char *) malloc(pri_len + 1);
    *pub_key = (char *) malloc(pub_len + 1);
    memset(*pri_key, 0, pri_len + 1);
    memset(*pub_key, 0, pub_len + 1);

    BIO_read(pri, *pri_key, pri_len);
    BIO_read(pub, *pub_key, pub_len);

    RSA_free(key_pair);
    BIO_free_all(pub);
    BIO_free_all(pri);
}

char *RSA_encrypt(const char *pub_key, const char *data) {
    RSA *p_rsa = NULL;
    BIO *bio = NULL;
    char *out = NULL;
    int rsa_len;

    if ((bio = BIO_new_mem_buf(pub_key, -1)) == NULL) {
        goto END;
    }

    if ((p_rsa = PEM_read_bio_RSAPublicKey(bio, NULL, NULL, NULL)) == NULL) {
        goto END;
    }

    rsa_len = RSA_size(p_rsa);
    if ((out = (char *) malloc(rsa_len + 1)) == NULL) {
        goto END;
    }
    memset(out, 0, rsa_len + 1);

    if(RSA_public_encrypt(strlen(data), (unsigned char *) data, (unsigned char *) out, p_rsa, RSA_PKCS1_PADDING) < 0) {
        free(out);
        out = NULL;
        goto END;
    }

    END:
    if (p_rsa != NULL) {
        RSA_free(p_rsa);
    }

    if (bio != NULL) {
        BIO_free_all(bio);
    }

    return out;
}

char *RSA_decrypt(const char *pri_key, const char *data) {
    RSA *p_rsa = NULL;
    BIO *bio = NULL;
    char *out = NULL;
    int rsa_len;

    if ((bio = BIO_new_mem_buf(pri_key, -1)) == NULL) {
        goto END;
    }

    if ((p_rsa = PEM_read_bio_RSAPrivateKey(bio, NULL, NULL, NULL)) == NULL) {
        goto END;
    }

    rsa_len = RSA_size(p_rsa);
    if ((out = (char *) malloc(rsa_len + 1)) == NULL) {
        goto END;
    }
    memset(out, 0, rsa_len + 1);

    if (RSA_private_decrypt(rsa_len, (unsigned char *) data, (unsigned char *) out, p_rsa, RSA_PKCS1_PADDING) < 0) {
        free(out);
        out = NULL;
        goto END;
    }

    END:
    if (p_rsa != NULL) {
        RSA_free(p_rsa);
    }

    if (bio != NULL) {
        BIO_free_all(bio);
    }

    return out;
}
```

