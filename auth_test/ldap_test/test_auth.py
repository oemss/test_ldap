import ldap


def check_ldap(userUid):
    connect = init()
    
    # try:
    #     connect.start_tls_s()
    # except ldap.OPERATIONS_ERROR as e:
    #     e_msg = e[0]['info']
    #     if e_msg == 'TLS already started':
    #         pass
    #     else:
    #         raise
    try:
        # if authentication successful, get the full user data
        connect.bind_s(user_dn, password)
        result = connect.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
        # return all user data results
        connect.unbind_s()
        print(result)
        print("Success")
    except ldap.LDAPError:
        connect.unbind_s()
        print("authentication error")


def init():
    ldap_server = "ldap://127.0.0.1"
    username = "Manager"
    password = "secret"
    # the following is the user_dn format provided by the ldap server
    user_dn = "cn=" + username + ",dc=maxcrc,dc=com"
    # adjust this to your base dn for searching
    base_dn = "dc=maxcrc,dc=com"
    return ldap.initialize(ldap_server)
