Building a brand new Security Guide based on a functional spec. The doc design was asked to be based off an existing doc that was fed into Claude

---

Read through this functional specification and create a customer facing document titled Extreme ONE OS Security Configuration Guide. The Security Configuration Guide must follow the same structure, design, style, and grammar of the attached SLX-20.4.1 Security Guide.

---

Convert this into a downloadable document and create table of contents

---



# Extreme ONE OS Security Configuration Guide

## Table of Contents

- [Preface](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#preface)
    - [Text Conventions](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#text-conventions)
    - [Documentation and Training](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#documentation-and-training)
    - [Help and Support](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#help-and-support)
    - [Subscribe to Product Announcements](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#subscribe-to-product-announcements)
    - [Send Feedback](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#send-feedback)
- [About this document](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#about-this-document)
    - [What's New in this Document](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#whats-new-in-this-document)
    - [Supported Hardware](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#supported-hardware)
- [Certificate Management](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#certificate-management)
    - [gNSI Certificate Management Overview](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#gnsi-certificate-management-overview)
    - [Understanding SSL Profiles](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#understanding-ssl-profiles)
    - [SSL Profile Management](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ssl-profile-management)
        - [Creating SSL Profiles](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#creating-ssl-profiles)
        - [Deleting SSL Profiles](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#deleting-ssl-profiles)
        - [Listing SSL Profiles](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#listing-ssl-profiles)
    - [Certificate Operations](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#certificate-operations)
        - [Importing Certificates](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#importing-certificates)
        - [Generating Certificates](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#generating-certificates)
        - [Viewing Certificates](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#viewing-certificates)
    - [Reserved SSL Profiles](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#reserved-ssl-profiles)
    - [Application SSL Profile Association](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#application-ssl-profile-association)
        - [gRPC Server Configuration](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#grpc-server-configuration)
        - [LDAP Configuration](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ldap-configuration)
        - [RADIUS Configuration](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#radius-configuration)
        - [Syslog Configuration](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#syslog-configuration)
    - [Token Validation](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#token-validation)
        - [Configuring Token Validator](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#configuring-token-validator)
        - [JWT Token Requirements](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#jwt-token-requirements)
    - [Certificate Monitoring](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#certificate-monitoring)
        - [Certificate Expiry Alerts](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#certificate-expiry-alerts)
        - [Viewing Certificate Status](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#viewing-certificate-status)
    - [Migration Procedures](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#migration-procedures)
    - [Best Practices](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#best-practices)
    - [Troubleshooting](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#troubleshooting)
    - [Security Considerations](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#security-considerations)
- [User Accounts and Passwords](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#user-accounts-and-passwords)
    - [User Account Overview](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#user-account-overview)
    - [Default Accounts and Roles](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#default-accounts-and-roles)
    - [Basic Account Management](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#basic-account-management)
        - [Creating an Admin-Role Account](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#creating-an-admin-role-account)
        - [Creating a User-Role Account](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#creating-a-user-role-account)
        - [Modifying an Account](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#modifying-an-account)
        - [Disabling an Account](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#disabling-an-account)
        - [Unlocking an Account](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#unlocking-an-account)
        - [Deleting an Account](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#deleting-an-account)
    - [Password Policies](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#password-policies)
    - [Service Password Encryption](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#service-password-encryption)
- [Remote Server Authentication](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#remote-server-authentication)
    - [Authentication Overview](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#authentication-overview)
    - [Login Authentication Mode](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#login-authentication-mode)
    - [RADIUS Configuration](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#radius-configuration-1)
        - [Adding a RADIUS Server](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#adding-a-radius-server)
        - [Enabling RADIUS over TLS (RadSec)](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#enabling-radius-over-tls-radsec)
    - [LDAP Configuration](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ldap-configuration-1)
        - [Adding an LDAP Server](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#adding-an-ldap-server)
        - [Enabling LDAP over TLS (LDAPS)](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#enabling-ldap-over-tls-ldaps)
    - [TACACS+ Configuration](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#tacacs-configuration)
        - [Adding a TACACS+ Server](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#adding-a-tacacs-server)
    - [OAuth2 Authentication](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#oauth2-authentication)
- [HTTPS Service Configuration](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#https-service-configuration)
    - [HTTPS Certificate Management](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#https-certificate-management)
        - [Generating HTTPS Certificate](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#generating-https-certificate)
        - [Importing HTTPS Certificate](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#importing-https-certificate)
        - [Configuring HTTPS Service](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#configuring-https-service)
- [Secure Shell (SSH)](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#secure-shell-ssh)
    - [SSH Overview](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ssh-overview)
    - [Configuring SSH Server](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#configuring-ssh-server)
        - [SSH Key Management](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ssh-key-management)
        - [SSH Ciphers](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ssh-ciphers)
        - [SSH MAC Algorithms](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ssh-mac-algorithms)
        - [SSH Key Exchange](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ssh-key-exchange)
    - [SSH Client Public Key Authentication](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ssh-client-public-key-authentication)
    - [SSH with x.509v3 Certificates](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#ssh-with-x509v3-certificates)
- [Access Control Lists (ACLs)](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#access-control-lists-acls)
    - [ACL Overview](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#acl-overview)
    - [Layer 2 (MAC) ACLs](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#layer-2-mac-acls)
    - [Layer 3 (IPv4/IPv6) ACLs](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#layer-3-ipv4ipv6-acls)
    - [ACL Best Practices](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#acl-best-practices)
- [Port Security](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#port-security)
    - [Port MAC Security Overview](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#port-mac-security-overview)
    - [Configuring Port Security](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#configuring-port-security)
    - [Sticky MAC Addresses](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#sticky-mac-addresses)
- [802.1X Authentication](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#8021x-authentication)
    - [802.1X Overview](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#8021x-overview)
    - [Basic 802.1X Configuration](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#basic-8021x-configuration)
    - [RADIUS Server for 802.1X](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#radius-server-for-8021x)
- [Mutual Authentication](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#mutual-authentication)
    - [Overview](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#overview)
    - [Configuring Mutual Authentication for Services](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#configuring-mutual-authentication-for-services)
- [Security Best Practices](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#security-best-practices)
    - [General Security Guidelines](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#general-security-guidelines)
    - [Certificate Management Best Practices](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#certificate-management-best-practices)
    - [Access Control Best Practices](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#access-control-best-practices)
    - [Network Security Best Practices](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#network-security-best-practices)
- [Troubleshooting Security Issues](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#troubleshooting-security-issues)
    - [Authentication Failures](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#authentication-failures)
    - [Certificate Problems](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#certificate-problems)
    - [ACL Issues](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#acl-issues)
- [Appendix A: Security Command Reference](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#appendix-a-security-command-reference)
- [Appendix B: Default Security Settings](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#appendix-b-default-security-settings)
- [Glossary](https://claude.ai/share/0253c19e-9632-473d-b114-461d83d0b3f9#glossary)

---

## Preface

### Text Conventions

Unless otherwise noted, information in this document applies to all supported environments for the products in question. Exceptions, like command keywords associated with a specific software version, are identified in the text.

When a feature, function, or operation pertains to a specific hardware product, the product name is used. When features, functions, and operations are the same across an entire product family, the product is referred to as the switch or the router.

**Table 1: Notes and warnings**

|Icon|Notice type|Alerts you to...|
|---|---|---|
|💡|Tip|Helpful tips and notices for using the product|
|📝|Note|Useful information or instructions|
|⚠️|Important|Important features or instructions|
|⚡|Caution|Risk of personal injury, system damage, or loss of data|
|🚫|Warning|Risk of severe personal injury|

**Table 2: Text**

|Convention|Description|
|---|---|
|`screen displays`|This typeface indicates command syntax, or represents information as it is displayed on the screen.|
|The words **enter** and **type**|When you see the word enter in this guide, you must type something, and then press the Return or Enter key. Do not press the Return or Enter key when an instruction simply says type.|
|Key names|Key names are written in boldface, for example **Ctrl** or **Esc**. If you must press two or more keys simultaneously, the key names are linked with a plus sign (+). Example: Press **Ctrl+Alt+Del**|
|_Words in italicized type_|Italics emphasize a point or denote new terms at the place where they are defined in the text. Italics are also used when referring to publication titles.|

**Table 3: Command syntax**

|Convention|Description|
|---|---|
|**bold text**|Bold text indicates command names, keywords, and command options.|
|_italic text_|Italic text indicates variable content.|
|[ ]|Syntax components displayed within square brackets are optional. Default responses to system prompts are enclosed in square brackets.|
|{ x \| y \| z }|A choice of required parameters is enclosed in curly brackets separated by vertical bars. You must select one of the options.|
|x \| y|A vertical bar separates mutually exclusive elements.|
|< >|Nonprinting characters, such as passwords, are enclosed in angle brackets.|
|...|Repeat the previous element, for example, member[member...].|
|\|In command examples, the backslash indicates a "soft" line break. When a backslash separates two lines of a command input, enter the entire command at the prompt without the backslash.|

### Documentation and Training

Find Extreme Networks product information at the following locations:

- Current Product Documentation
- Release Notes
- Hardware and software compatibility for Extreme Networks products
- Extreme Optics Compatibility
- Other resources such as white papers, data sheets, and case studies

Extreme Networks offers product training courses, both online and in person, as well as specialized certifications. For details, visit www.extremenetworks.com/education/.

### Help and Support

If you require assistance, contact Extreme Networks using one of the following methods:

**Extreme Portal** Search the GTAC (Global Technical Assistance Center) knowledge base; manage support cases and service contracts; download software; and obtain product licensing, training, and certifications.

**The Hub** A forum for Extreme Networks customers to connect with one another, answer questions, and share ideas and feedback. This community is monitored by Extreme Networks employees, but is not intended to replace specific guidance from GTAC.

**Call GTAC** For immediate support: (800) 998 2408 (toll-free in U.S. and Canada) or 1 (408) 579 2826. For the support phone number in your country, visit: www.extremenetworks.com/support/contact

Before contacting Extreme Networks for technical support, have the following information ready:

- Your Extreme Networks service contract number, or serial numbers for all involved Extreme Networks products
- A description of the failure
- A description of any actions already taken to resolve the problem
- A description of your network environment (such as layout, cable type, other relevant environmental information)
- Network load at the time of trouble (if known)
- The device history (for example, if you have returned the device before, or if this is a recurring problem)
- Any related RMA (Return Material Authorization) numbers

### Subscribe to Product Announcements

You can subscribe to email notifications for product and software release announcements, Field Notices, and Vulnerability Notices.

1. Go to The Hub.
2. In the list of categories, expand the Product Announcements list.
3. Select a product for which you would like to receive notifications.
4. Select Subscribe.
5. To select additional products, return to the Product Announcements list and repeat steps 3 and 4.

You can modify your product selections or unsubscribe at any time.

### Send Feedback

The Information Development team at Extreme Networks has made every effort to ensure that this document is accurate, complete, and easy to use. We strive to improve our documentation to help you in your work, so we want to hear from you. We welcome all feedback, but we especially want to know about:

- Content errors, or confusing or conflicting information.
- Improvements that would help you find relevant information.
- Broken links or usability issues.

To send feedback, do either of the following:

- Access the feedback form at https://www.extremenetworks.com/documentation-feedback/.
- Email us at documentation@extremenetworks.com.

Provide the publication title, part number, and as much detail as possible, including the topic heading and page number if applicable, as well as your suggestions for improvement.

## About this document

### What's New in this Document

This document includes comprehensive coverage of the new gNSI Certificate Management feature, which provides standardized certificate management capabilities through gRPC-based services. Key additions include:

- gNSI Certificate Management service implementation
- SSL profile management and association
- Token validation for external user authentication
- Enhanced certificate monitoring and expiry alerts
- Migration procedures for upgrades and downgrades

For additional information, refer to the Extreme ONE OS Release Notes for this version.

### Supported Hardware

Extreme ONE OS runs on all platforms that support the SR (Service Router) application, including:

- ExtremeSwitching platforms with SR capabilities
- ExtremeRouting platforms with SR capabilities

> **Note**: All configurations and software features that are applicable to specific hardware platforms are identified where relevant throughout this guide.

## Certificate Management

### gNSI Certificate Management Overview

gNSI (gRPC Network Security Interface) provides a standardized way to manage network security configurations and operations on devices. The gNSI Certificate Management service (Certz) facilitates certificate management within network devices by enabling secure communication using TLS/SSL certificates.

The gNSI Certz service replaces the deprecated gNOI certificate management service, providing improved certificate management capabilities with granular control over individual certificates and certificate authorities.

### Understanding SSL Profiles

SSL profiles are containers that include various security artifacts:

- Application certificates (with public key and private key)
- CA (Certificate Authority) trust bundles
- Certificate chains

Each SSL profile can be associated with multiple applications, allowing efficient certificate management across services.

### SSL Profile Management

#### Creating SSL Profiles

To create a new SSL profile:

```
device# certificate-manager add-profile ssl-profile-id <profile-name>
```

> **Note**: SSL profile names must be unique and cannot begin with "ssl-reserved" which is reserved for system use.

#### Deleting SSL Profiles

To delete an SSL profile:

```
device# certificate-manager delete ssl-profile-id <profile-name>
```

> **Important**: You cannot delete an SSL profile that is currently associated with an application. Remove all associations before deletion.

#### Listing SSL Profiles

To view all SSL profiles on the device:

```
device# show certificate-manager ssl-profiles
```

### Certificate Operations

#### Importing Certificates

To import an application certificate with private key:

```
device# certificate-manager import ssl-profile-id <profile-name> application-certificate 
        protocol <scp|ftp> host <host-address> certificate <file-path> 
        user <username> password <password> vrf <vrf-name>
```

To import a CA trust certificate:

```
device# certificate-manager import ssl-profile-id <profile-name> ca-trust-certificate 
        protocol <scp|ftp> host <host-address> certificate <file-path> 
        user <username> password <password> vrf <vrf-name>
```

#### Generating Certificates

To generate a self-signed certificate:

```
device# certificate-manager generate ssl-profile-id <profile-name> 
        certificate-extension san <ip-address>
```

#### Viewing Certificates

To display certificates in an SSL profile:

```
device# show certificate-manager certificates <profile-name>
device# show certificate-manager ca-certificates <profile-name>
```

### Reserved SSL Profiles

The system maintains several reserved SSL profiles for specific purposes:

#### ssl-reserved-generated

Used by gRPC server instances for generated certificates.

#### ssl-reserved-ztp

Stores CA certificates downloaded during secure Zero Touch Provisioning workflows.

#### ssl-reserved-https

Contains CA certificates necessary for firmware updates and copy operations using HTTPS.

### Application SSL Profile Association

#### gRPC Server Configuration

To associate an SSL profile with a gRPC server instance:

```
device(config)# system
device(config-system)# grpc-server <instance-name>
device(config-system-grpc-server)# certificate-id <ssl-profile-id>
device(config-system-grpc-server)# enable
```

> **Note**: After updating the SSL profile, restart the gRPC server instance for changes to take effect.

#### LDAP Configuration

To configure LDAP with SSL profile association:

```
device(config)# system
device(config-system)# aaa
device(config-system-aaa)# server-group ldap
device(config-system-aaa-server-group-ldap)# server <server-address>
device(config-system-aaa-server-group-ldap-server)# ssl-profile-id <profile-name>
device(config-system-aaa-server-group-ldap-server)# ldaps
```

#### RADIUS Configuration

To configure RADIUS with SSL profile association:

```
device(config)# system
device(config-system)# aaa
device(config-system-aaa)# server-group radius
device(config-system-aaa-server-group-radius)# server <server-address>
device(config-system-aaa-server-group-radius-server)# ssl-profile-id <profile-name>
device(config-system-aaa-server-group-radius-server)# radsec
```

#### Syslog Configuration

To configure secure syslog with SSL profile:

```
device(config)# system
device(config-system)# logging
device(config-system-logging)# remote-server <server-address>
device(config-system-logging-remote-server)# secure-forwarding tls
device(config-system-logging-remote-server)# tls-profile-id <profile-name>
```

### Token Validation

Token validation enables authentication of external users through JWT (JSON Web Token) tokens included in gNMI requests.

#### Configuring Token Validator

```
device(config)# system
device(config-system)# aaa
device(config-system-aaa)# token-validator <instance-name>
device(config-system-aaa-token-validator)# ssl-profile-id <profile-name>
```

#### JWT Token Requirements

JWT tokens must include the following claims:

- `sub`: Subject (username)
- `role`: User role (e.g., admin, user)
- `exp`: Expiration timestamp
- `iat`: Issued at timestamp

### Certificate Monitoring

#### Certificate Expiry Alerts

Configure certificate expiry alerts to receive notifications before certificates expire:

```
device(config)# expiry-alert info period <days>
device(config)# expiry-alert warning period <days>
device(config)# expiry-alert critical period <days>
```

Alert levels:

- **Info**: 60 days before expiry (configurable)
- **Warning**: 30 days before expiry (configurable)
- **Critical**: 7 days before expiry (configurable)
- **Error**: Certificate has expired (automatic daily alerts)

#### Viewing Certificate Status

To check certificate validity and associations:

```
device# show certificate-manager ca-certificates <profile-name>
```

This displays:

- Certificate details
- Validity period
- Applications using the certificate

### Migration Procedures

#### Upgrading from Legacy Certificate Management

When upgrading from systems using gNOI certificate management to gNSI:

1. **Remove existing certificates**:
    
    ```
    device# certificate-manager delete ssl-profile-id all
    ```
    
2. **Import certificates to new SSL profiles**:
    
    - Create SSL profiles for each application
    - Import appropriate certificates
    - Associate profiles with applications
3. **Restart affected services**:
    
    - gRPC server instances
    - Syslog daemon (if applicable)

#### Downgrade Considerations

When downgrading to legacy certificate management:

1. **Document current SSL profile associations**
2. **Export certificates if needed**
3. **Remove all gNSI-managed certificates**:
    
    ```
    device# certificate-manager delete all
    ```
    
4. **Reconfigure using legacy commands**

### Best Practices

1. **Use descriptive SSL profile names** that indicate their purpose
2. **Regularly monitor certificate expiry** using the alert system
3. **Maintain separate SSL profiles** for different applications when possible
4. **Test certificate updates** in a maintenance window
5. **Document SSL profile associations** for disaster recovery

### Troubleshooting

#### Common Issues

**Certificate import fails**

- Verify network connectivity to the certificate server
- Check file permissions and path
- Ensure certificate format is PEM
- Verify certificate validity period includes current time

**Application cannot use certificate**

- Confirm SSL profile association is correct
- Verify certificate chain is complete
- Check certificate purpose matches application needs
- Restart application after certificate updates

**Certificate expiry alerts not received**

- Verify expiry alert configuration
- Check system time is accurate
- Ensure syslog is properly configured

#### Debug Commands

```
device# show certificate-manager ssl-profiles
device# show certificate-manager certificates <profile-name>
device# show certificate-manager ca-certificates <profile-name>
device# show logging raslog | include certificate
```

### Security Considerations

1. **Protect private keys**: Use secure protocols (SCP) when importing certificates
2. **Limit SSL profile access**: Use role-based access control
3. **Regular certificate rotation**: Plan for certificate renewal before expiry
4. **Verify certificate chains**: Ensure complete trust chains are imported
5. **Monitor certificate usage**: Track which applications use which certificates

## User Accounts and Passwords

### User Account Overview

A user account specifies that user's level of access to the device CLI. The software uses role-based access control (RBAC) as the authorization mechanism.

### Default Accounts and Roles

The software ships with two default accounts:

- **admin**: Accounts with admin permissions can execute all commands supported on the device
- **user**: Accounts with user-level permissions can execute all show commands and basic operational commands

### Basic Account Management

#### Creating an Admin-Role Account

```
device# configure terminal
device(config)# username jsmith role admin password StrongPass123! 
                desc "Has access to all commands"
```

#### Creating a User-Role Account

```
device# configure terminal
device(config)# username jdoe role user password UserPass456!
```

#### Modifying an Account

```
device# configure terminal
device(config)# username jdoe role admin
```

#### Disabling an Account

```
device# configure terminal
device(config)# username testUser enable false
```

> **Note**: Disabling an account immediately terminates all active sessions for that user.

#### Unlocking an Account

```
device# unlock username testUser
Result: Unlocking the user account is successful
```

#### Deleting an Account

```
device# configure terminal
device(config)# no username testUser
```

### Password Policies

Configure password policies to enforce security requirements:

```
device# configure terminal
device(config)# password-attributes min-length 12 max-retry 5 
                character-restriction lower 2 upper 2 numeric 2 special-char 1
```

Password policy parameters:

- **min-length**: Minimum password length (8-32 characters)
- **max-retry**: Failed login attempts before lockout (0-16)
- **character-restriction**: Required character types
- **history**: Number of previous passwords to check against
- **repeat**: Consecutive repetitive characters allowed
- **sequence**: Consecutive sequential characters allowed

### Service Password Encryption

Enable password encryption for all user accounts:

```
device# configure terminal
device(config)# service password-encryption
```

## Remote Server Authentication

### Authentication Overview

Extreme ONE OS supports multiple authentication protocols:

- **RADIUS**: Remote Authentication Dial-In User Service
- **LDAP**: Lightweight Directory Access Protocol with Active Directory
- **TACACS+**: Terminal Access Controller Access-Control System Plus
- **OAuth2**: Token-based authentication

### Login Authentication Mode

Configure the authentication order:

```
device# configure terminal
device(config)# aaa authentication login <primary> [secondary]
```

Examples:

- `aaa authentication login radius local`
- `aaa authentication login ldap local-auth-fallback`
- `aaa authentication login tacacs+ local`

### RADIUS Configuration

#### Adding a RADIUS Server

```
device# configure terminal
device(config)# system
device(config-system)# aaa
device(config-system-aaa)# server-group radius
device(config-system-aaa-server-group-radius)# server 10.10.10.100
device(config-system-aaa-server-group-radius-server)# secret-key MySecretKey123
device(config-system-aaa-server-group-radius-server)# auth-port 1812
device(config-system-aaa-server-group-radius-server)# network-instance mgmt-vrf
```

#### Enabling RADIUS over TLS (RadSec)

```
device(config-system-aaa-server-group-radius-server)# radsec
device(config-system-aaa-server-group-radius-server)# ssl-profile-id radius-ssl
device(config-system-aaa-server-group-radius-server)# auth-port 2083
```

### LDAP Configuration

#### Adding an LDAP Server

```
device# configure terminal
device(config)# system
device(config-system)# aaa
device(config-system-aaa)# server-group ldap
device(config-system-aaa-server-group-ldap)# server ldap.company.com
device(config-system-aaa-server-group-ldap-server)# base-dn "dc=company,dc=com"
device(config-system-aaa-server-group-ldap-server)# port 389
device(config-system-aaa-server-group-ldap-server)# network-instance mgmt-vrf
```

#### Enabling LDAP over TLS (LDAPS)

```
device(config-system-aaa-server-group-ldap-server)# ldaps
device(config-system-aaa-server-group-ldap-server)# ssl-profile-id ldap-ssl
device(config-system-aaa-server-group-ldap-server)# port 636
```

### TACACS+ Configuration

#### Adding a TACACS+ Server

```
device# configure terminal
device(config)# tacacs-server host 10.10.10.200 use-vrf mgmt-vrf
device(config-tacacs-server)# key SharedSecret789
device(config-tacacs-server)# port 49
device(config-tacacs-server)# timeout 10
```

### OAuth2 Authentication

OAuth2 authentication allows token-based authentication for northbound interfaces.

#### Configuring OAuth2

```
device# configure terminal
device(config)# aaa authentication login oauth2 local-auth-fallback
```

#### Importing OAuth2 PKI Certificate

```
device# certificate-manager import ssl-profile-id oauth2-profile 
        ca-trust-certificate protocol scp host 10.10.10.50 
        certificate /certs/oauth2-ca.pem user admin password secret
```

## HTTPS Service Configuration

### HTTPS Certificate Management

HTTPS service requires proper certificate configuration for secure web access.

#### Generating HTTPS Certificate

```
device# certificate-manager generate ssl-profile-id https-profile 
        certificate-extension san device.company.com
```

#### Importing HTTPS Certificate

```
device# certificate-manager import ssl-profile-id https-profile 
        application-certificate protocol scp host 10.10.10.50 
        certificate /certs/device.pem user admin password secret
```

#### Configuring HTTPS Service

```
device# configure terminal
device(config)# http server use-vrf mgmt-vrf
device(config-http-server)# secure-port 443
device(config-http-server)# ssl-profile-id https-profile
device(config-http-server)# no shutdown
```

## Secure Shell (SSH)

### SSH Overview

Secure Shell (SSH) provides encrypted remote access connections to network devices.

### Configuring SSH Server

#### SSH Key Management

Configure SSH host keys:

```
device# configure terminal
device(config)# ssh server key rsa 2048
device(config)# ssh server key ecdsa 256
```

#### SSH Ciphers

Configure allowed SSH ciphers:

```
device# configure terminal
device(config)# ssh server cipher aes256-ctr,aes192-ctr,aes128-ctr
device(config)# ssh client cipher aes256-ctr,aes192-ctr,aes128-ctr
```

#### SSH MAC Algorithms

Configure SSH MAC algorithms:

```
device# configure terminal
device(config)# ssh server mac hmac-sha2-256,hmac-sha2-512
device(config)# ssh client mac hmac-sha2-256,hmac-sha2-512
```

#### SSH Key Exchange

Configure key exchange algorithms:

```
device# configure terminal
device(config)# ssh server key-exchange ecdh-sha2-nistp256,diffie-hellman-group14-sha256
```

### SSH Client Public Key Authentication

#### Importing SSH Client Keys

```
device# certutil import sshkey directory /keys/ file id_rsa.pub 
        host 10.10.10.50 login admin password secret 
        protocol scp user deviceadmin
```

#### Direct Public Key Configuration

```
device# certutil sshkey user admin pubkey "ssh-rsa AAAAB3NzaC1yc2EAAA..."
```

### SSH with x.509v3 Certificates

Configure SSH authentication using x.509v3 certificates:

```
device# configure terminal
device(config)# ssh server algorithm hostkey x509v3-ssh-rsa
device(config)# ssh server certificate profile server
device(config-ssh-server-cert-profile)# trustpoint sign ssh-x509-profile
```

## Access Control Lists (ACLs)

### ACL Overview

Access Control Lists filter network traffic based on specified criteria.

### Layer 2 (MAC) ACLs

#### Creating a MAC ACL

```
device# configure terminal
device(config)# mac access-list extended test_mac_01
device(conf-macl-ext)# seq 10 permit host 0022.3333.4444 any
device(conf-macl-ext)# seq 20 deny any any
```

#### Applying MAC ACL to Interface

```
device# configure terminal
device(config)# interface ethernet 0/1
device(conf-if-eth-0/1)# mac access-group test_mac_01 in
```

### Layer 3 (IPv4/IPv6) ACLs

#### Creating IPv4 ACL

```
device# configure terminal
device(config)# ip access-list extended web_filter
device(conf-ipacl-ext)# seq 10 permit tcp any any eq 80
device(conf-ipacl-ext)# seq 20 permit tcp any any eq 443
device(conf-ipacl-ext)# seq 30 deny ip any any
```

#### Creating IPv6 ACL

```
device# configure terminal
device(config)# ipv6 access-list extended ipv6_filter
device(conf-ip6acl-ext)# seq 10 permit tcp any any eq 80
device(conf-ip6acl-ext)# seq 20 deny ipv6 any any
```

### ACL Best Practices

1. Use descriptive ACL names
2. Document ACL rules with remarks
3. Order rules from most specific to least specific
4. Include explicit deny rules when needed
5. Test ACLs before production deployment

## Port Security

### Port MAC Security Overview

Port MAC security limits the number of MAC addresses that can be learned on an interface.

### Configuring Port Security

```
device# configure terminal
device(config)# interface ethernet 0/1
device(conf-if-eth-0/1)# switchport
device(conf-if-eth-0/1)# switchport port-security
device(conf-if-eth-0/1)# switchport port-security max 5
device(conf-if-eth-0/1)# switchport port-security violation shutdown
device(conf-if-eth-0/1)# switchport port-security shutdown-time 300
```

### Sticky MAC Addresses

Enable sticky MAC learning:

```
device(conf-if-eth-0/1)# switchport port-security sticky
```

## 802.1X Authentication

### 802.1X Overview

IEEE 802.1X provides port-based network access control.

### Basic 802.1X Configuration

#### Global 802.1X Enable

```
device# configure terminal
device(config)# dot1x enable
```

#### Interface 802.1X Configuration

```
device# configure terminal
device(config)# interface ethernet 0/1
device(conf-if-eth-0/1)# dot1x authentication
device(conf-if-eth-0/1)# dot1x port-control auto
```

#### 802.1X Reauthentication

```
device(conf-if-eth-0/1)# dot1x reauthentication
device(conf-if-eth-0/1)# dot1x timeout re-authperiod 3600
```

### RADIUS Server for 802.1X

Configure RADIUS server for 802.1X authentication:

```
device# configure terminal
device(config)# radius-server host 10.10.10.100 use-vrf mgmt-vrf
device(config-radius-server)# key MyRadiusKey123
device(config-radius-server)# auth-port 1812
```

## Mutual Authentication

### Overview

Mutual authentication ensures both client and server verify each other's identity.

### Configuring Mutual Authentication for Services

#### HTTPS Mutual Authentication

1. Import server certificate:

```
device# certificate-manager import ssl-profile-id https-mutual 
        application-certificate protocol scp host 10.10.10.50 
        certificate /certs/server.pem user admin password secret
```

2. Import client CA certificate:

```
device# certificate-manager import ssl-profile-id https-mutual 
        ca-trust-certificate protocol scp host 10.10.10.50 
        certificate /certs/client-ca.pem user admin password secret
```

3. Configure HTTPS service:

```
device(config)# http server use-vrf mgmt-vrf
device(config-http-server)# ssl-profile-id https-mutual
device(config-http-server)# client-auth required
```

#### gRPC Mutual Authentication

Configure gRPC with mutual TLS:

```
device(config)# system
device(config-system)# grpc-server default
device(config-system-grpc-server)# certificate-id grpc-mutual
device(config-system-grpc-server)# client-auth required
device(config-system-grpc-server)# enable
```

## Security Best Practices

### General Security Guidelines

1. **Change default credentials** immediately after installation
2. **Use strong passwords** meeting complexity requirements
3. **Enable service password encryption**
4. **Configure login banners** with appropriate warnings
5. **Implement AAA** for centralized authentication
6. **Use secure protocols** (SSH, HTTPS, SNMPv3)
7. **Disable unused services** and ports
8. **Configure timeouts** for idle sessions
9. **Enable logging** for security events
10. **Regularly update** firmware and certificates

### Certificate Management Best Practices

1. **Use separate SSL profiles** for different services
2. **Monitor certificate expiry** with alerts
3. **Implement certificate rotation** procedures
4. **Secure private key storage** and transmission
5. **Verify certificate chains** are complete
6. **Document certificate dependencies**
7. **Test certificate updates** before production

### Access Control Best Practices

1. **Implement defense in depth** with multiple security layers
2. **Use ACLs** to restrict management access
3. **Configure port security** on access ports
4. **Enable 802.1X** for network access control
5. **Implement RADIUS/TACACS+** for centralized control
6. **Use role-based access control** (RBAC)
7. **Audit user activities** regularly
8. **Configure accounting** for compliance

### Network Security Best Practices

1. **Segment networks** using VLANs
2. **Implement broadcast storm control**
3. **Configure DHCP snooping** where appropriate
4. **Enable dynamic ARP inspection**
5. **Use private VLANs** for isolation
6. **Configure BPDU guard** on access ports
7. **Implement IP source guard**
8. **Monitor for security anomalies**

## Troubleshooting Security Issues

### Authentication Failures

#### Diagnosing Login Issues

1. Check authentication order:

```
device# show running-config aaa authentication
```

2. Verify server connectivity:

```
device# ping <server-ip> vrf <vrf-name>
```

3. Check server configuration:

```
device# show running-config radius-server
device# show running-config ldap-server
device# show running-config tacacs-server
```

4. Review authentication logs:

```
device# show logging raslog | include auth
```

### Certificate Problems

#### Certificate Validation Failures

1. Check certificate validity:

```
device# show certificate-manager certificates <profile-name>
```

2. Verify certificate chain:

```
device# show certificate-manager ca-certificates <profile-name>
```

3. Check system time:

```
device# show clock
```

4. Review certificate logs:

```
device# show logging raslog | include certificate
```

### ACL Issues

#### Traffic Not Being Filtered

1. Verify ACL configuration:

```
device# show access-list
```

2. Check ACL application:

```
device# show access-list interface ethernet 0/1
```

3. Review ACL statistics:

```
device# show statistics access-list
```

## Appendix A: Security Command Reference

### Certificate Management Commands

|Command|Description|
|---|---|
|`certificate-manager add-profile`|Create new SSL profile|
|`certificate-manager delete`|Delete SSL profile or certificates|
|`certificate-manager generate`|Generate self-signed certificate|
|`certificate-manager import`|Import certificates|
|`show certificate-manager`|Display certificate information|

### Authentication Commands

|Command|Description|
|---|---|
|`aaa authentication login`|Configure login authentication|
|`aaa accounting`|Configure accounting|
|`aaa authorization`|Configure authorization|
|`radius-server host`|Configure RADIUS server|
|`ldap-server host`|Configure LDAP server|
|`tacacs-server host`|Configure TACACS+ server|

### Access Control Commands

|Command|Description|
|---|---|
|`ip access-list`|Configure IPv4 ACL|
|`ipv6 access-list`|Configure IPv6 ACL|
|`mac access-list`|Configure MAC ACL|
|`show access-list`|Display ACL information|

## Appendix B: Default Security Settings

### Default Account Settings

- Default admin password: admin
- Default user password: user
- Password minimum length: 8 characters
- Account lockout threshold: Disabled (0)
- Password encryption: Enabled

### Default Service Settings

- SSH: Enabled on all VRFs
- Telnet: Disabled
- HTTP: Disabled
- HTTPS: Disabled when no certificates configured
- SNMP: Community string "public" (read-only)

### Default Timeout Settings

- CLI idle timeout: 30 minutes
- SSH timeout: 120 seconds
- RADIUS timeout: 5 seconds
- TACACS+ timeout: 5 seconds

## Glossary

**AAA**: Authentication, Authorization, and Accounting

**ACL**: Access Control List

**CA**: Certificate Authority

**gNMI**: gRPC Network Management Interface

**gNSI**: gRPC Network Security Interface

**JWT**: JSON Web Token

**LDAP**: Lightweight Directory Access Protocol

**RADIUS**: Remote Authentication Dial-In User Service

**RBAC**: Role-Based Access Control

**SSL**: Secure Sockets Layer

**TACACS+**: Terminal Access Controller Access-Control System Plus

**TLS**: Transport Layer Security