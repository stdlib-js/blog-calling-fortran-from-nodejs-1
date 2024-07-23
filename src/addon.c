// file: addon.c

#include "mul_fortran.h"
#include <node_api.h>
#include <assert.h>

/**
* Receives JavaScript callback invocation data.
*
* @param env    environment under which the function is invoked
* @param info   callback data
* @return       Node-API value
*/
static napi_value addon( napi_env env, napi_callback_info info ) {
	napi_status status;

	// Define the expected number of input arguments:
	size_t argc = 2;

	// Retrieve the input arguments from the callback info:
	napi_value argv[ 2 ];
	status = napi_get_cb_info( env, info, &argc, argv, NULL, NULL );
	assert( status == napi_ok );

	// Convert each argument to a signed 32-bit integer:
	int x;
	status = napi_get_value_int32( env, argv[ 0 ], &x );
	assert( status == napi_ok );

	int y;
	status = napi_get_value_int32( env, argv[ 1 ], &y );
	assert( status == napi_ok );

	// Call the Fortran routine:
	int res;
	mul( &x, &y, &res );

	// Convert the result to a JavaScript object:
	napi_value out;
	status = napi_create_int32( env, res, &out );
	assert( status == napi_ok );

	return out;
}

/**
* Defines the Node.js module "exports" object for the native add-on.
*
* @param env      environment under which the function is invoked
* @param exports  exports object
* @return         Node-API value
*/
static napi_value Init( napi_env env, napi_value exports ) {
	napi_value fcn;

	// Export the add-on function as a "default" export:
	napi_status status = napi_create_function( env, "exports", NAPI_AUTO_LENGTH, addon, NULL, &fcn );

	// Verify that we successfully wrapped the `addon` function as a JavaScript function object:
	assert( status == napi_ok );

	// Return the JavaScript function object to allow registering with the JavaScript runtime:
	return fcn;
}

/**
* Register a Node-API module which exports a function.
*/
NAPI_MODULE( NODE_GYP_MODULE_NAME, Init )
