#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <gmp.h>

static void perform_rsa(mpz_t result, mpz_t message, mpz_t d, mpz_t n);
static void usage();
static int hex_to_ascii(char a, char b);
static int hex_to_int(char a);

int main(int argc, char **argv) {

    mpz_t result, message, d, n;
    FILE *message_file, *d_file, *n_file;
    size_t bytes_read;
    int c, i, err, option_index;
    char *result_str;
    message_file = d_file = n_file = 0;
    option_index = 0;
    err = 0;

    static struct option long_options[] = {
	{"message", required_argument, 0, 'm'},
	{"exp", required_argument, 0, 'd'},
	{"modulus", required_argument, 0, 'n'},
	{0, 0, 0, 0},
    };

    while (1) {
	c = getopt_long(argc, argv, "d:n:m:", long_options, &option_index);
	if (c < 0) {
	    break;
	}
	switch(c) {
	case 0:
            usage();
	    break;
	case 'd':
	    d_file = fopen(optarg, "r");
	    if (d_file == NULL) {
		perror("Key file error");
		exit(1);
	    }
	    break;
	case 'm':
	    message_file = fopen(optarg, "r");
	    if (message_file == NULL) {
		perror("Message file error");
		exit(1);
	    }
	    break;
	case 'n':
	    n_file = fopen(optarg, "r");
	    if (n_file == NULL) {
		perror("Modulus file error");
		exit(1);
	    }
	    break;
	case '?':
	    usage();
	    break;
	default:
	    usage();
	    break;
	}
    }

    if (message_file == NULL || n_file == NULL || d_file == NULL) {
        usage();
    }

    mpz_init(result);
    mpz_init(message);
    bytes_read = mpz_inp_str(message, message_file, 0);
    if (bytes_read <= 0) {
	err = 1;
    }
    mpz_init(d);
    bytes_read = mpz_inp_str(d, d_file, 0);
    if (bytes_read <= 0) {
	err = 1;
    }
    mpz_init(n);
    bytes_read = mpz_inp_str(n, n_file, 0);
    if (bytes_read <= 0) {
	err = 1;
    }

    if (err == 1) {
	printf("%s\n", "Error: cannot read one or more files. See spec for usage.");
	exit(1);
    }

    /* Computes RSA using the specified parameters and stores the value in RESULT. */
    perform_rsa(result, message, d, n);

    result_str = mpz_get_str(NULL, 16, result);
    i = 0;
    while(result_str[i] != '\0') {
	printf("%c", hex_to_ascii(result_str[i], result_str[i+1]));
	i+=2;
    }

    mpz_clear(result);
    mpz_clear(message);
    mpz_clear(d);

    return 0;
}

/*
 * @param result: a field to populate with the result of your RSA calculation.
 * @param message: the message to perform RSA on. (probably a cert in this case)
 * @param e: the encryption key from the key_file passed in through the command-line arguments
 * @param n: the modulus for RSA from the modulus_file passed in through the command-line arguments
 *

 */
static void
perform_rsa(mpz_t result, mpz_t message, mpz_t d, mpz_t n)
{
    /* YOUR CODE HERE */
    // 14.76 Algorithm - right to left exponentiation

    // Given g and integer e for exponentiation
        // g = message. decryt = d. Modulo = n
    
    // a  = 1, S = message
        // A is the result we will return. S is the message
    // while d != 0
    //     if d is odd, then a = a*s
    //     d = d/2
    //     if d != 0, then s = s*s
    // return a

    //Initialize variables. 
    mpz_t res;

    // mpz_init(s);
    
    mpz_init(res);

    // mpz_add(s, s, message);    

    mpz_set_str(result, "1", 10);

    while(mpz_cmp_ui(d, 0) > 0 ){
        mpz_mod_ui(res, d, 2);
        
        if (mpz_cmp_ui(res, 0) > 0){
            // printf("This is an odd");
            mpz_mul(result, result, message);
            // Add in the mod
            mpz_mod(result, result, n);
        }

        mpz_div_ui(d, d, 2);

        if (mpz_cmp_ui(d, 0) != 0){
            mpz_mul(message, message, message);

            //Adding in the mod

            mpz_mod(message, message, n);
        }


    }

    mpz_clear(res); 


    




    





    // while (mpz_cmpr(d, e) != 0){
    //     if (e ){

    //     }

    // gmp_printf ("%s is an mpz %Zd\n", "here", d);

    // mpz_init(e);
    // mpz_init(m);


    // char g;

    // mpz_get_str(g, 10, message);
    // mpz_init_set_str(e, *d, 10);
    // mpz_init_set_str(m, *n, 10)s;





    





}

static void
usage()
{


    // TESTING HERE
    mpz_t base, d, n, result;
    // //Sets to 0
    mpz_init(base);
    mpz_init(d);
    mpz_init(n);
    mpz_init(result);


    // gmp_printf ("%s is an mpz %Zd\n", "here", base);
    mpz_set_str(base, "10", 10);
    mpz_set_str(d, "11", 10);
    mpz_set_str(n, "21", 10);
    // gmp_printf ("%s is an mpz  %Zd\n", "here", base);


    perform_rsa(result, base, d, n);

    gmp_printf ("%s is the result  %Zd\n", "here", result);







    // mpz_add(a, a, z);
    
    // //How to assign gmp variables
    // gmp_printf ("%s is an mpz aaa %Zd\n", "here", a);

    // TESTING HERE







    printf("./proj0 -m <message_file> -n <modulus_file> -d <key_file>\n");
    exit(1);
}

static int
hex_to_ascii(char a, char b)
{
    int high = hex_to_int(a) * 16;
    int low = hex_to_int(b);
    return high + low;
}

static int
hex_to_int(char a)
{
    if (a >= 97) {
	a -= 32;
    }
    int first = a / 16 - 3;
    int second = a % 16;
    int result = first*10 + second;
    if (result > 9) {
	result -= 1;
    }
    return result;
}
