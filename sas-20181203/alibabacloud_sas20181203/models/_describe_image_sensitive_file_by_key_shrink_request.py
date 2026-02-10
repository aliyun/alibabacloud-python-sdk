# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageSensitiveFileByKeyShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        image_uuid: str = None,
        lang: str = None,
        page_size: int = None,
        scan_range_shrink: str = None,
        sensitive_file_key: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The type of the asset that you want to scan. Valid values:
        # 
        # *   **image**
        # *   **container**
        self.scan_range_shrink = scan_range_shrink
        # The type of alerts for the sensitive files. Valid values:
        # 
        # *   **npm_token**: Node Package Manager (NPM) access token
        # *   **ftp_cfg**: FTP configuration
        # *   **google_oauth_key**: Google OAuth key
        # *   **planetscale_passwd**: PlanetScale password
        # *   **github_ssh_key**: Github SSH key
        # *   **msbuild_publish_profile**: MSBuild publish profile
        # *   **fastly_cdn_token**: Fastly CDN token
        # *   **ssh_private_key**: SSH private key
        # *   **aws_cli**: Amazon Web Services (AWS) CLI credentials
        # *   **cpanel_proftpd**: cPanel ProFTPD credentials
        # *   **postgresql_passwd**: PostgreSQL password
        # *   **discord_client_cred**: Discord client credentials
        # *   **rails_database**: Rails database configuration
        # *   **aws_access_key**: AWS Access Key
        # *   **esmtp_cfg** :Extended Simple Mail Transfer Protocol (ESMTP) configuration
        # *   **docker_registry_cfg**: Docker image repository configuration
        # *   **pem**: Privacy-Enhanced Mail (PEM)
        # *   **common_cred**: common credentials
        # *   **sftp_cfg**: Secure File Transfer Protocol (SFTP) connection configuration
        # *   **grafana_token**: Grafana token
        # *   **slack_token**: Slack token
        # *   **ec_private_key**: EC private key
        # *   **pypi_token**: Python Package Index (PyPI) token
        # *   **finicity_token**: Finicity token
        # *   **k8s_client_key**: Kubernetes private key
        # *   **git_cfg**: Git configuration
        # *   **django_key**: Django key
        # *   **jenkins_ssh**: Jenkins SSH configuration file
        # *   **openssh_private_key**: OpenSSL private key
        # *   **square_oauth**: OAuth credential for Square
        # *   **typeform_token**: Typeform token
        # *   **common_database_cfg**: general database connection configuration
        # *   **wordpress_database_cfg**: WordPress database configuration
        # *   **googlecloud_api_key**: API key for Google Cloud
        # *   **vscode_sftp**: VSCode SFTP configuration
        # *   **apache_htpasswd**: Apache htpasswd
        # *   **planetscale_token**: PlanetScale token
        # *   **contentful_preview_token**: preview token for Contentful
        # *   **php_database_cfg**: database password for a PHP application
        # *   **atom_remote_sync**: Atom remote synchronization configuration
        # *   **aws_session_token**: AWS session token
        # *   **atom_sftp_cfg**: Atom SFTP configuration
        # *   **asana_client_private_key**: Asana client key
        # *   **tencentcloud_ak**: secret ID of a third-party cloud
        # *   **rsa_private_key**: Rivest-Shamir-Adleman (RSA) private key
        # *   **github_personal_token**: personal access token for GitHub
        # *   **pgp**: Pretty Good Privacy (PGP) encrypted file
        # *   **stripe_skpk**: Stripe secret key
        # *   **square_token**: Square access token
        # *   **rails_carrierwave**: Rails Carrierwave credential
        # *   **dbeaver_database_cfg**: DBeaver database configuration
        # *   **robomongo_cred**: Robomongo credentials
        # *   **github_oauth_token**: OAuth access token for GitHub
        # *   **pulumi_token**: Pulumi token
        # *   **ventrilo_voip**: Ventrilo VoIP server configuration
        # *   **macos_keychain**: macOS Keychain
        # *   **amazon_mws_token**: Amazon MWS token
        # *   **dynatrace_token**: Dynatrace token
        # *   **java_keystore**: Java KeyStore (JKS)
        # *   **microsoft_sdf**: Microsoft SQL Server Compact Edition (CE) database
        # *   **kubernetes_dashboard_cred**: user credentials for Kubernetes Dashboard
        # *   **atlassian_token**: Atlassian token
        # *   **rdp**: remote desktop protocol (RDP)
        # *   **mailgun_key**: Mailgun webhook signing key
        # *   **mailchimp_api_key**: API key for Mailchimp
        # *   **netrc_cfg**: .netrc configuration file
        # *   **openvpn_cfg**: OpenVPN configuration
        # *   **github_refresh_token**: GitHub refresh token
        # *   **salesforce**: Salesforce credentials
        # *   **salesforce**: Sendinblue credentials
        # *   **pkcs_private_key**: PKCS#12 key
        # *   **rubyonrails_passwd**: Ruby on Rails password file
        # *   **filezilla_ftp**: FileZilla FTP configuration
        # *   **databricks_token**: Databricks token
        # *   **gitLab_personal_toke**: personal access token for GitLab
        # *   **rails_master_key**: Rails master key
        # *   **sqlite**: SQLite3 or SQLite database
        # *   **firefox_logins**: Firefox logon configuration
        # *   **mailgun_private_token**: Mailgun private token
        # *   **joomla_cfg**: Joomla configuration
        # *   **hashicorp_terraform_token**: HashiCorp Terraform token
        # *   **jetbrains_ides**: JetBrains IDEs configuration
        # *   **heroku_api_key**: Heroku API key
        # *   **messagebird_token**: MessageBird token
        # *   **messagebird_token**: MessageBird token
        # *   **hashicorp_vault_token**: HashiCorp Vault token
        # *   **pgp_private_key**: PGP private key
        # *   **sshpasswd**: SSH password
        # *   **huaweicloud_ak**: secret access key of a third-party cloud
        # *   **aws_s3cmd**: AWS S3cmd configuration
        # *   **php_config**: PHP configuration
        # *   **common_private_key**: private key of a common type
        # *   **microsoft_mdf**: Microsoft SQL Server database
        # *   **mediawiki_cfg**: MediaWiki configuration
        # *   **jenkins_cred**: Jenkins credentials
        # *   **rubygems_cred**: RubyGems credentials
        # *   **clojars_token**: Clojars token
        # *   **phoenix_web_passwd**: Phoenix web credentials
        # *   **puttygen_private_key**: PuTTYgen private key
        # *   **google_oauth_token**: Google OAuth access token
        # *   **rubyonrails_cfg**: Ruby On Rails database configuration
        # *   **lob_api_key**: Lob API key
        # *   **pkcs_cred**: PKCS#12 certificate
        # *   **otr_private_key**: Off-the-Record Messaging (OTR) private key
        # *   **contentful_delivery_token**: delivery token for Contentful
        # *   **digital_ocean_tugboat**: DigitalOcean Tugboat configuration
        # *   **dsa_private_key**: Digital Signature Algorithm (DSA) private key
        # *   **rails_app_token**: Rails app token
        # *   **git_cred**: Git user credential
        # *   **newrelic_api_key**: User API key for New Relic
        # *   **github_hub**: hub configuration for storing GitHub tokens
        # *   **rubygem**: Rubygem Token
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

        if self.scan_range_shrink is not None:
            result['ScanRange'] = self.scan_range_shrink

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
            self.scan_range_shrink = m.get('ScanRange')

        if m.get('SensitiveFileKey') is not None:
            self.sensitive_file_key = m.get('SensitiveFileKey')

        return self

