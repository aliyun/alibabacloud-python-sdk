# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImageSensitiveFileListRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        criteria_type: str = None,
        current_page: int = None,
        image_uuid: str = None,
        lang: str = None,
        page_size: int = None,
        risk_level: str = None,
        scan_range: List[str] = None,
        sensitive_key_list: List[str] = None,
    ):
        # The value that corresponds to the search type.
        self.criteria = criteria
        # The search type for sensitive files. Valid values:
        # 
        # - **SensitiveFileKey**: the sensitive file alerting categorization. Valid values:
        # 
        #     - **npm_token**: NPM access token
        #     - **ftp_cfg**: FTP configuration
        #     - **google_oauth_key**: Google OAuth Key
        #     - **planetscale_passwd**: Planetscale password
        #     - **github_ssh_key**: Github SSH key
        #     - **msbuild_publish_profile**: MSBuild publish profile
        #     - **fastly_cdn_token**: Fastly CDN token
        #     - **ssh_private_key**: SSH private key
        #     - **aws_cli**: AWS CLI credentials
        #     - **cpanel_proftpd**: cPanel ProFTPd credentials
        #     - **postgresql_passwd**: PostgreSQL password file
        #     - **discord_client_cred**: Discord client credentials
        #     - **rails_database**: Rails database configuration
        #     - **aws_access_key**: AWS Access Key
        #     - **esmtp_cfg**: ESMTP mail server configuration
        #     - **docker_registry_cfg**: Docker image repository configuration
        #     - **pem**: PEM
        #     - **common_cred**: common credentials
        #     - **sftp_cfg**: SFTP connection configuration
        #     - **grafana_token**: Grafana token
        #     - **slack_token**: Slack Token
        #     - **ec_private_key**: EC private key
        #     - **pypi_token**: PyPI upload token
        #     - **finicity_token**: Finicity platform token
        #     - **k8s_client_key**: Kubernetes client private key
        #     - **git_cfg**: Git configuration
        #     - **django_key**: Django key
        #     - **jenkins_ssh**: Jenkins SSH configuration file
        #     - **openssh_private_key**: OPENSSH private key
        #     - **square_oauth**: Square OAuth credentials
        #     - **typeform_token**: Typeform token
        #     - **common_database_cfg**: common database connection configuration
        #     - **wordpress_database_cfg**: WordPress database configuration
        #     - **googlecloud_api_key**: Google Cloud API Key
        #     - **vscode_sftp**: VSCode SFTP configuration
        #     - **apache_htpasswd**: Apache htpasswd
        #     - **planetscale_token**: Planetscale token
        #     - **contentful_preview_token**: Contentful Preview token
        #     - **php_database_cfg**: PHP application database password
        #     - **atom_remote_sync**: Atom remote synchronization configuration
        #     - **aws_session_token**: AWS session token
        #     - **atom_sftp_cfg**: Atom SFTP configuration
        #     - **asana_client_private_key**: Asana client private key
        #     - **tencentcloud_ak**: third-party cloud SecretId
        #     - **rsa_private_key**: RSA private key
        #     - **github_personal_token**: Github Personal access token
        #     - **pgp**: PGP encrypt file
        #     - **stripe_skpk**: Stripe Secret Key
        #     - **square_token**: Square access token
        #     - **rails_carrierwave**: Rails Carrierwave file upload credentials
        #     - **dbeaver_database_cfg**: DBeaver database configuration
        #     - **robomongo_cred**: Robomongo credentials
        #     - **github_oauth_token**: Github OAuth access token
        #     - **pulumi_token**: Pulumi token
        #     - **ventrilo_voip**: Ventrilo VoIP Server configuration
        #     - **macos_keychain**: macOS Keychain
        #     - **amazon_mws_token**: Amazon MWS Token
        #     - **dynatrace_token**: Dynatrace token
        #     - **java_keystore**: Java KeyStore
        #     - **microsoft_sdf**: Microsoft SQL CE database
        #     - **kubernetes_dashboard_cred**: Kubernetes Dashboard user credentials
        #     - **atlassian_token**: Atlassian token
        #     - **rdp**: Remote Desktop Protocol (RDP) connection
        #     - **mailgun_key**: Mailgun Webhook Signing Key
        #     - **mailchimp_api_key**: Mailchimp API Key
        #     - **netrc_cfg**: .netrc configuration file
        #     - **openvpn_cfg**: OpenVPN client configuration
        #     - **github_refresh_token**: Github Refresh Token
        #     - **salesforce**: Salesforce credentials
        #     - **sendinblue**: Sendinblue token
        #     - **pkcs_private_key**: PKCS#12 key
        #     - **rubyonrails_passwd**: Ruby on Rails password file
        #     - **filezilla_ftp**: FileZilla FTP configuration
        #     - **databricks_token**: Databricks token
        #     - **gitLab_personal_token**: GitLab Personal access token
        #     - **rails_master_key**: Rails Master Key
        #     - **sqlite**: SQLite3/SQLite database
        #     - **firefox_logins**: Firefox logon configuration
        #     - **mailgun_private_token**: Mailgun Private token
        #     - **joomla_cfg**: Joomla configuration
        #     - **hashicorp_terraform_token**: Hashicorp Terraform Token
        #     - **jetbrains_ides**: Jetbrains IDEs configuration
        #     - **heroku_api_key**: Heroku API key
        #     - **messagebird_token**: MessageBird token
        #     - **github_app_token**: Github App Token
        #     - **hashicorp_vault_token**: Hashicorp Vault Token
        #     - **pgp_private_key**: PGP private key
        #     - **sshpasswd**: SSH password
        #     - **huaweicloud_ak**: third-party cloud Secret Access Key
        #     - **aws_s3cmd**: AWS S3cmd configuration
        #     - **php_config**: PHP configuration
        #     - **common_private_key**: common private key types
        #     - **microsoft_mdf**: Microsoft SQL database
        #     - **mediawiki_cfg**: MediaWiki configuration
        #     - **jenkins_cred**: Jenkins credentials
        #     - **rubygems_cred**: Rubygems credentials
        #     - **clojars_token**: Clojars token
        #     - **phoenix_web_passwd**: Phoenix Web credentials
        #     - **puttygen_private_key**: PuTTYgen private key
        #     - **google_oauth_token**: Google OAuth access token
        #     - **rubyonrails_cfg**: Ruby On Rails database configuration
        #     - **lob_api_key**: Lob API Key
        #     - **pkcs_cred**: PKCS#12 certificate
        #     - **otr_private_key**: OTR private key
        #     - **contentful_delivery_token**: Contentful Delivery token
        #     - **digital_ocean_tugboat**: Digital Ocean Tugboat configuration
        #     - **dsa_private_key**: DSA private key
        #     - **rails_app_token**: Rails App token
        #     - **git_cred**: Git user credentials
        #     - **newrelic_api_key**: New Relic User API Key
        #     - **github_hub**: hub configuration that stores Github tokens
        #     - **rubygem**: Rubygem token
        # - **SensitiveFileName**: the sensitive file alerting type.
        self.criteria_type = criteria_type
        # The page number of the page to return. Minimum value: **1**. Default value: **1**.
        self.current_page = current_page
        # The unique identifier of the image.
        # > Call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation of Container Registry. You can obtain the unique identifier of the container image from the **ImageUuid** response parameter.
        self.image_uuid = image_uuid
        # The language of the content in the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return on each page in a paging query. Default value: 20.
        self.page_size = page_size
        # The risk level. Valid values:
        # 
        # - **high**: high
        # 
        # - **medium**: medium
        # 
        # - **low**: low.
        self.risk_level = risk_level
        # The collection of scan scopes. Valid values:
        # 
        # - **image**: image.
        # - **container**: container.
        self.scan_range = scan_range
        # The list of sensitive file keys.
        self.sensitive_key_list = sensitive_key_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.criteria_type is not None:
            result['CriteriaType'] = self.criteria_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.sensitive_key_list is not None:
            result['SensitiveKeyList'] = self.sensitive_key_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CriteriaType') is not None:
            self.criteria_type = m.get('CriteriaType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('SensitiveKeyList') is not None:
            self.sensitive_key_list = m.get('SensitiveKeyList')

        return self

