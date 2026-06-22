# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageListBySensitiveFileShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        image_digest: str = None,
        lang: str = None,
        page_size: int = None,
        repo_instance_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        risk_level: str = None,
        scan_range_shrink: str = None,
        sensitive_file_key: str = None,
        status: str = None,
    ):
        # The page number of the current page to return. Minimum value: 1. Default value: 1.
        self.current_page = current_page
        # The image digest.
        # > Fuzzy search is supported.
        self.image_digest = image_digest
        # Sets the language type for request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return on each page in a paginated query. Default value: 20.
        self.page_size = page_size
        # The ID of the container image instance.
        # > You can call the [ListRepository](https://help.aliyun.com/document_detail/451339.html) operation of Container Registry to obtain the container image instance ID from the **InstanceId** response parameter.
        self.repo_instance_id = repo_instance_id
        # The name of the image repository.
        # > Fuzzy search is supported.
        self.repo_name = repo_name
        # The namespace of the image repository.
        # > Fuzzy search is supported.
        self.repo_namespace = repo_namespace
        # The risk level of the file. Separate multiple levels with commas (,). Valid values:
        # 
        # - **high**: High risk.
        # - **medium**: Medium risk.
        # - **low**: Low risk.
        self.risk_level = risk_level
        # The collection of scan scopes. Valid values:
        # 
        # - **image**: Image.
        # - **container**: Container.
        self.scan_range_shrink = scan_range_shrink
        # The type of sensitive file alert. Valid values:
        # 
        # - **npm_token**: NPM access token
        # - **ftp_cfg**: FTP configuration
        # - **google_oauth_key**: Google OAuth Key
        # - **planetscale_passwd**: Planetscale password
        # - **github_ssh_key**: GitHub SSH key
        # - **msbuild_publish_profile**: MSBuild publish profile
        # - **fastly_cdn_token**: Fastly CDN token
        # - **ssh_private_key**: SSH private key
        # - **aws_cli**: AWS CLI credentials
        # - **cpanel_proftpd**: cPanel ProFTPd credentials
        # - **postgresql_passwd**: PostgreSQL password file
        # - **discord_client_cred**: Discord client credentials
        # - **rails_database**: Rails database configuration
        # - **aws_access_key**: AWS Access Key
        # - **esmtp_cfg**: ESMTP mail server configuration
        # - **docker_registry_cfg**: Docker image registry configuration
        # - **pem**: PEM
        # - **common_cred**: Common credentials
        # - **sftp_cfg**: SFTP connection configuration
        # - **grafana_token**: Grafana token
        # - **slack_token**: Slack Token
        # - **ec_private_key**: EC private key
        # - **pypi_token**: PyPI upload token
        # - **finicity_token**: Finicity platform token
        # - **k8s_client_key**: Kubernetes client private key
        # - **git_cfg**: Git configuration
        # - **django_key**: Django key
        # - **jenkins_ssh**: Jenkins SSH configuration file
        # - **openssh_private_key**: OpenSSH private key
        # - **square_oauth**: Square OAuth credentials
        # - **typeform_token**: Typeform token
        # - **common_database_cfg**: Common database connection configuration
        # - **wordpress_database_cfg**: WordPress database configuration
        # - **googlecloud_api_key**: Google Cloud API Key
        # - **vscode_sftp**: VSCode SFTP configuration
        # - **apache_htpasswd**: Apache htpasswd
        # - **planetscale_token**: Planetscale token
        # - **contentful_preview_token**: Contentful Preview token
        # - **php_database_cfg**: PHP application database password
        # - **atom_remote_sync**: Atom remote sync configuration
        # - **aws_session_token**: AWS session token
        # - **atom_sftp_cfg**: Atom SFTP configuration
        # - **asana_client_private_key**: Asana project management platform client key
        # - **tencentcloud_ak**: Third-party cloud SecretId
        # - **rsa_private_key**: RSA private key
        # - **github_personal_token**: GitHub Personal access token
        # - **pgp**: PGP encrypted file
        # - **stripe_skpk**: Stripe Secret Key
        # - **square_token**: Square access token
        # - **rails_carrierwave**: Rails Carrierwave file upload credentials
        # - **dbeaver_database_cfg**: DBeaver database configuration
        # - **robomongo_cred**: Robomongo credentials
        # - **github_oauth_token**: GitHub OAuth access token
        # - **pulumi_token**: Pulumi token
        # - **ventrilo_voip**: Ventrilo VoIP Server configuration
        # - **macos_keychain**: macOS Keychain
        # - **amazon_mws_token**: Amazon MWS Token
        # - **dynatrace_token**: Dynatrace token
        # - **java_keystore**: Java Keystore
        # - **microsoft_sdf**: Microsoft SQL CE database
        # - **kubernetes_dashboard_cred**: Kubernetes Dashboard user credentials
        # - **atlassian_token**: Atlassian token
        # - **rdp**: Remote Desktop Connection RDP
        # - **mailgun_key**: Mailgun Webhook Signing Key
        # - **mailchimp_api_key**: Mailchimp API Key
        # - **netrc_cfg**: .netrc configuration file
        # - **openvpn_cfg**: OpenVPN client configuration
        # - **github_refresh_token**: GitHub Refresh Token
        # - **salesforce**: Salesforce credentials
        # - **sendinblue**: Sendinblue token
        # - **pkcs_private_key**: PKCS#12 key
        # - **rubyonrails_passwd**: Ruby on Rails password file
        # - **filezilla_ftp**: FileZilla FTP configuration
        # - **databricks_token**: Databricks token
        # - **gitLab_personal_token**: GitLab Personal access token
        # - **rails_master_key**: Rails Master Key
        # - **sqlite**: SQLite3/SQLite database
        # - **firefox_logins**: Firefox login configuration
        # - **mailgun_private_token**: Mailgun Private token
        # - **joomla_cfg**: Joomla configuration
        # - **hashicorp_terraform_token**: HashiCorp Terraform Token
        # - **jetbrains_ides**: JetBrains IDEs configuration
        # - **heroku_api_key**: Heroku API key
        # - **messagebird_token**: MessageBird token
        # - **github_app_token**: GitHub App Token
        # - **hashicorp_vault_token**: HashiCorp Vault Token
        # - **pgp_private_key**: PGP private key
        # - **sshpasswd**: SSH password
        # - **huaweicloud_ak**: Third-party cloud Secret Access Key
        # - **aws_s3cmd**: AWS S3cmd configuration
        # - **php_config**: PHP configuration
        # - **common_private_key**: Common private key type
        # - **microsoft_mdf**: Microsoft SQL database
        # - **mediawiki_cfg**: MediaWiki configuration
        # - **jenkins_cred**: Jenkins credentials
        # - **rubygems_cred**: RubyGems credentials
        # - **clojars_token**: Clojars token
        # - **phoenix_web_passwd**: Phoenix Web credentials
        # - **puttygen_private_key**: PuTTYgen private key
        # - **google_oauth_token**: Google OAuth access token
        # - **rubyonrails_cfg**: Ruby on Rails database configuration
        # - **lob_api_key**: Lob API Key
        # - **pkcs_cred**: PKCS#12 certificate
        # - **otr_private_key**: OTR private key
        # - **contentful_delivery_token**: Contentful Delivery token
        # - **digital_ocean_tugboat**: Digital Ocean Tugboat configuration
        # - **dsa_private_key**: DSA private key
        # - **rails_app_token**: Rails App token
        # - **git_cred**: Git user credentials
        # - **newrelic_api_key**: New Relic User API Key
        # - **github_hub**: Hub configuration storing GitHub tokens
        # - **rubygem**: RubyGem token
        self.sensitive_file_key = sensitive_file_key
        # The status of the sensitive file. Valid values:
        # - **0**: Unhandled.
        # - **1**: Ignored.
        # - **2**: False positive.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.scan_range_shrink is not None:
            result['ScanRange'] = self.scan_range_shrink

        if self.sensitive_file_key is not None:
            result['SensitiveFileKey'] = self.sensitive_file_key

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('ScanRange') is not None:
            self.scan_range_shrink = m.get('ScanRange')

        if m.get('SensitiveFileKey') is not None:
            self.sensitive_file_key = m.get('SensitiveFileKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

