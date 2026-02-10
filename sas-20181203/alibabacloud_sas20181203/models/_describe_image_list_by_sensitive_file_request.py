# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImageListBySensitiveFileRequest(DaraModel):
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
        scan_range: List[str] = None,
        sensitive_file_key: str = None,
        status: str = None,
    ):
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # The image digest.
        # > Fuzzy match is supported.
        self.image_digest = image_digest
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The ID of the specified container image.
        # 
        # > You can call the [ListRepository](https://help.aliyun.com/document_detail/451339.html) operation to obtain the IDs of container images from the value of the **InstanceId** response parameter.
        self.repo_instance_id = repo_instance_id
        # The name of the image repository.
        # 
        # > Fuzzy match is supported.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        # > Fuzzy match is supported.
        self.repo_namespace = repo_namespace
        # The risk level of the file. Separate multiple levels with commas (,). Valid values:
        # 
        # - **high**
        # - **medium**
        # - **low**
        self.risk_level = risk_level
        # An array consisting of the types of the assets that you want to scan. Valid values:
        # - **image**
        # - **container**
        self.scan_range = scan_range
        # The type of the alert for the sensitive file. Valid values:
        # 
        # *   **npm_token**: npm access token.
        # *   **ftp_cfg**: FTP configuration.
        # *   **google_oauth_key**: Google OAuth key.
        # *   **planetscale_passwd**: PlanetScale password.
        # *   **github_ssh_key**: Github SSH key.
        # *   **msbuild_publish_profile**: MSBuild publish profile.
        # *   **fastly_cdn_token**: Fastly CDN token.
        # *   **ssh_private_key**: SSH private key.
        # *   **aws_cli**: Amazon Web Services (AWS) CLI credential.
        # *   **cpanel_proftpd**: cPanel ProFTPD credential.
        # *   **postgresql_passwd**: PostgreSQL password file.
        # *   **discord_client_cred**: Discord client credential.
        # *   **rails_database**: Rails database configuration.
        # *   **aws_access_key**: AWS access key.
        # *   **esmtp_cfg**: configuration of mail server over Extended Simple Mail Transfer Protocol (ESMTP).
        # *   **docker_registry_cfg**: configuration of a Docker image repository.
        # *   **pem**: Privacy-Enhanced Mail (PEM).
        # *   **common_cred**: common credential.
        # *   **sftp_cfg**: configuration of connection over Secure File Transfer Protocol (SFTP).
        # *   **grafana_token**: Grafana token.
        # *   **slack_token**: Slack token.
        # *   **ec_private_key**: Elliptic Curve (EC) private key.
        # *   **pypi_token**: Python Package Index (PyPI) token.
        # *   **finicity_token**: Finicity token.
        # *   **k8s_client_key**: private key for the Kubernetes client.
        # *   **git_cfg**: Git configuration.
        # *   **django_key**: Django key.
        # *   **jenkins_ssh**: SSH configuration file for Jenkins.
        # *   **openssh_private_key**: OpenSSH private key.
        # *   **square_oauth**: Square OAuth credential.
        # *   **typeform_token**: Typeform token.
        # *   **common_database_cfg**: configuration of general database connection.
        # *   **wordpress_database_cfg**: WordPress database configuration.
        # *   **googlecloud_api_key**: API key for Google Cloud.
        # *   **vscode_sftp**: VSCode SFTP configuration.
        # *   **apache_htpasswd**: Apache htpasswd.
        # *   **planetscale_token**: PlanetScale token.
        # *   **contentful_preview_token**: preview token for Contentful.
        # *   **php_database_cfg**: database password for a PHP application.
        # *   **atom_remote_sync**: Atom remote synchronization configuration.
        # *   **aws_session_token**: AWS session token.
        # *   **atom_sftp_cfg**: Atom SFTP configuration.
        # *   **asana_client_private_key**: private key for the Asana client.
        # *   **tencentcloud_ak**: secret ID of a third-party cloud.
        # *   **rsa_private_key**: Rivest-Shamir-Adleman (RSA) private key.
        # *   **github_personal_token**: personal access token for GitHub.
        # *   **pgp**: Pretty Good Privacy (PGP) encrypted file.
        # *   **stripe_skpk**: Stripe secret key.
        # *   **square_token**: Square access token.
        # *   **rails_carrierwave**: Rails Carrierwave credential.
        # *   **dbeaver_database_cfg**: DBeaver database configuration.
        # *   **robomongo_cred**: RoboMongo credential.
        # *   **github_oauth_token**: OAuth access token for GitHub.
        # *   **pulumi_token**: Pulumi token.
        # *   **ventrilo_voip**: configuration of a Ventrilo VoIP server.
        # *   **macos_keychain**: macOS keychain.
        # *   **amazon_mws_token**: Amazon MWS token.
        # *   **dynatrace_token**: Dynatrace token.
        # *   **java_keystore**: Java KeyStore (JKS).
        # *   **microsoft_sdf**: Microsoft SQL Server Compact Edition (CE) database.
        # *   **kubernetes_dashboard_cred**: user credential for Kubernetes Dashboard.
        # *   **atlassian_token**: Atlassian token.
        # *   **rdp**: remote desktop protocol (RDP).
        # *   **mailgun_key**: Mailgun webhook signing key.
        # *   **mailchimp_api_key**: API key for Mailchimp.
        # *   **netrc_cfg**: .netrc configuration file.
        # *   **openvpn_cfg**: configuration of the OpenVPN client.
        # *   **github_refresh_token**: GitHub refresh token.
        # *   **salesforce**: Salesforce credential.
        # *   **salesforce**: Sendinblue token.
        # *   **pkcs_private_key**: PKCS#12 private key.
        # *   **rubyonrails_passwd**: Ruby on Rails password file.
        # *   **filezilla_ftp**: FileZilla FTP configuration.
        # *   **databricks_token**: Databricks token.
        # *   **gitLab_personal_toke**: personal access token for GitLab.
        # *   **rails_master_key**: Rails master key.
        # *   **sqlite**: SQLite3 or SQLite database.
        # *   **firefox_logins**: Firefox logon configuration.
        # *   **mailgun_private_token**: Mailgun private token.
        # *   **joomla_cfg**: Joomla configuration.
        # *   **hashicorp_terraform_token**: HashiCorp Terraform token.
        # *   **jetbrains_ides**: JetBrains IDEs configuration.
        # *   **heroku_api_key**: API key for Heroku.
        # *   **messagebird_token**: MessageBird token.
        # *   **github_app_token**: Github app token.
        # *   **hashicorp_vault_token**: HashiCorp Vault token.
        # *   **pgp_private_key**: PGP private key.
        # *   **sshpasswd**: SSH password.
        # *   **huaweicloud_ak**: secret access key of a third-party cloud.
        # *   **aws_s3cmd**: AWS S3cmd configuration.
        # *   **php_config**: PHP configuration.
        # *   **common_private_key**: common private key.
        # *   **microsoft_mdf**: Microsoft SQL Server database.
        # *   **mediawiki_cfg**: MediaWiki configuration.
        # *   **jenkins_cred**: Jenkins credential.
        # *   **rubygems_cred**: RubyGems credential.
        # *   **clojars_token**: Clojars token.
        # *   **phoenix_web_passwd**: Phoenix web credential.
        # *   **puttygen_private_key**: PuTTYgen private key.
        # *   **google_oauth_token**: Google OAuth access token.
        # *   **rubyonrails_cfg**: Ruby On Rails database configuration.
        # *   **lob_api_key**: Lob API key for Lob.
        # *   **pkcs_cred**: PKCS#12 certificate.
        # *   **otr_private_key**: Off-the-Record Messaging (OTR) private key.
        # *   **contentful_delivery_token**: Contentful delivery token.
        # *   **digital_ocean_tugboat**: DigitalOcean Tugboat configuration.
        # *   **dsa_private_key**: Digital Signature Algorithm (DSA) private key.
        # *   **rails_app_token**: app token for Rails.
        # *   **git_cred**: user credential for Git.
        # *   **newrelic_api_key**: User API key for New Relic.
        # *   **github_hub**: hub configuration for storing GitHub tokens.
        # *   **rubygem**: RubyGem token.
        self.sensitive_file_key = sensitive_file_key
        # The sensitive file status. Valid values:
        # 
        # *   **0**: unhandled
        # *   **1**: ignored
        # *   **2**: false positive
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

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

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
            self.scan_range = m.get('ScanRange')

        if m.get('SensitiveFileKey') is not None:
            self.sensitive_file_key = m.get('SensitiveFileKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

