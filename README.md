## Usage Instructions

1) First, create an azure add application.

    * "Allow public client flows" must be enabled
    * An API must be exposed, even if no scopes are defined
    * The application needs to be assigned graph API permissions that you desire
    * The application needs to be provisioned a client secret

2) From a python interpreter, do the following

    * import obo_wash
    * tenant_id = < id of target tenant >
    * client_id = < id of application created in step 1 >
    * client_secret = < secret assigned to application in step 1 >
    * creds = obo_wash.obo_existing_application(tenant_id, client_id, client_secret)

3) Creds now contains an access_token and a refresh_token. If you wish to obtain a new access token, do the following

    * new_creds = obo_wash.authenticate_client_credentials_flow(tenant_id, client_id, client_secret, access_token, obo=False)




