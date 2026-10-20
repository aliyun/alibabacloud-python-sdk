# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImageSensitiveFileByKeyRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        image_uuid: str = None,
        lang: str = None,
        page_size: int = None,
        scan_range: List[str] = None,
        sensitive_file_key: str = None,
    ):
        # The page number of the returned page. Default value: **1**.
        self.current_page = current_page
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The maximum number of entries to return on each page in a paging query. Default value: **20**.
        self.page_size = page_size
        # The scan scope. Valid values:
        # 
        # - **image**: image
        # - **container**: container
        self.scan_range = scan_range
        # The alerting type of the sensitive file. Valid values:
        # 
        # - **npm_token**: NPM access token
        # - **ftp_cfg**: FTP configuration
        # - **google_oauth_key**: Google OAuth key
        # - **planetscale_passwd**: Planetscale password
        # - **github_ssh_key**: GitHub SSH key
        # - **msbuild_publish_profile**: MSBuild publish profile
        # - **fastly_cdn_token**: Fastly CDN token
        # - **ssh_private_key**: SSH private key
        # - **aws_cli**: AWS CLI credential
        # - **cpanel_proftpd**: cPanel ProFTPd credential
        # - **postgresql_passwd**: PostgreSQL password file
        # - **discord_client_cred**: Discord client credential
        # - **rails_database**: Rails database configuration
        # - **aws_access_key**: AWS access key
        # - **esmtp_cfg**: ESMTP mail server configuration
        # - **docker_registry_cfg**: Docker image repository configuration
        # - **pem**: PEM
        # - **common_cred**: common credential
        # - **sftp_cfg**: SFTP connection configuration
        # - **grafana_token**: Grafana token
        # - **slack_token**: Slack token
        # - **ec_private_key**: EC private key
        # - **pypi_token**: PyPI upload token
        # - **finicity_token**: Finicity platform token
        # - **k8s_client_key**: Kubernetes client private key
        # - **git_cfg**: Git configuration
        # - **django_key**: Django key
        # - **jenkins_ssh**: Jenkins SSH configuration file
        # - **openssh_private_key**: OpenSSH private key
        # - **square_oauth**: Square OAuth credential
        # - **typeform_token**: Typeform token
        # - **common_database_cfg**: common database connection configuration
        # - **wordpress_database_cfg**: WordPress database configuration
        # - **googlecloud_api_key**: Google Cloud API key
        # - **vscode_sftp**: VSCode SFTP configuration
        # - **apache_htpasswd**: Apache htpasswd
        # - **planetscale_token**: Planetscale token
        # - **contentful_preview_token**: Contentful preview token
        # - **php_database_cfg**: PHP application database password
        # - **atom_remote_sync**: Atom remote synchronization configuration
        # - **aws_session_token**: AWS session token
        # - **atom_sftp_cfg**: Atom SFTP configuration
        # - **asana_client_private_key**: Asana project management platform client key
        # - **tencentcloud_ak**: SecretId of other cloud service providers
        # - **rsa_private_key**: RSA private key
        # - **github_personal_token**: GitHub personal access token
        # - **pgp**: PGP encrypted file
        # - **stripe_skpk**: Stripe secret key
        # - **square_token**: Square access token
        # - **rails_carrierwave**: Rails Carrierwave file upload credential
        # - **dbeaver_database_cfg**: DBeaver database configuration
        # - **robomongo_cred**: Robomongo credential
        # - **github_oauth_token**: GitHub OAuth access token
        # - **pulumi_token**: Pulumi token
        # - **ventrilo_voip**: Ventrilo VoIP server configuration
        # - **macos_keychain**: macOS keychain
        # - **amazon_mws_token**: Amazon MWS token
        # - **dynatrace_token**: Dynatrace token
        # - **java_keystore**: Java keystore
        # - **microsoft_sdf**: Microsoft SQL CE database
        # - **kubernetes_dashboard_cred**: Kubernetes Dashboard user credential
        # - **atlassian_token**: Atlassian token
        # - **rdp**: Remote Desktop Protocol (RDP) connection
        # - **mailgun_key**: Mailgun webhook signing key
        # - **mailchimp_api_key**: Mailchimp API key
        # - **netrc_cfg**: .netrc configuration file
        # - **openvpn_cfg**: OpenVPN client configuration
        # - **github_refresh_token**: GitHub refresh token
        # - **salesforce**: Salesforce credential
        # - **sendinblue**: Sendinblue token
        # - **pkcs_private_key**: PKCS#12 key
        # - **rubyonrails_passwd**: Ruby on Rails password file
        # - **filezilla_ftp**: FileZilla FTP configuration
        # - **databricks_token**: Databricks token
        # - **gitLab_personal_token**: GitLab personal access token
        # - **rails_master_key**: Rails master key
        # - **sqlite**: SQLite3/SQLite database
        # - **firefox_logins**: Firefox logon configuration
        # - **mailgun_private_token**: Mailgun private token
        # - **joomla_cfg**: Joomla configuration
        # - **hashicorp_terraform_token**: HashiCorp Terraform token
        # - **jetbrains_ides**: JetBrains IDEs configuration
        # - **heroku_api_key**: Heroku API key
        # - **messagebird_token**: MessageBird token
        # - **github_app_token**: GitHub app token
        # - **hashicorp_vault_token**: HashiCorp Vault token
        # - **pgp_private_key**: PGP private key
        # - **sshpasswd**: SSH password
        # - **huaweicloud_ak**: Secret access key of other cloud service providers
        # - **aws_s3cmd**: AWS S3cmd configuration
        # - **php_config**: PHP configuration
        # - **common_private_key**: common private key type
        # - **microsoft_mdf**: Microsoft SQL database
        # - **mediawiki_cfg**: MediaWiki configuration
        # - **jenkins_cred**: Jenkins credential
        # - **rubygems_cred**: RubyGems credential
        # - **clojars_token**: Clojars token
        # - **phoenix_web_passwd**: Phoenix web credential
        # - **puttygen_private_key**: PuTTYgen private key
        # - **google_oauth_token**: Google OAuth access token
        # - **rubyonrails_cfg**: Ruby on Rails database configuration
        # - **lob_api_key**: Lob API key
        # - **pkcs_cred**: PKCS#12 certificate
        # - **otr_private_key**: OTR private key
        # - **contentful_delivery_token**: Contentful delivery token
        # - **digital_ocean_tugboat**: DigitalOcean Tugboat configuration
        # - **dsa_private_key**: DSA private key
        # - **rails_app_token**: Rails app token
        # - **git_cred**: Git user credential
        # - **newrelic_api_key**: New Relic user API key
        # - **github_hub**: Hub configuration that stores GitHub tokens
        # - **rubygem**: RubyGems token
        self.sensitive_file_key = sensitive_file_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.sensitive_file_key is not None:
            result['SensitiveFileKey'] = self.sensitive_file_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('SensitiveFileKey') is not None:
            self.sensitive_file_key = m.get('SensitiveFileKey')

        return self

