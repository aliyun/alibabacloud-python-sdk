# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetImageSensitiveFileStatusRequest(DaraModel):
    def __init__(
        self,
        id_list: List[int] = None,
        image_uuids: str = None,
        scan_range: List[str] = None,
        sensitive_file_key: str = None,
        status: int = None,
    ):
        # The IDs of the sensitive files.
        self.id_list = id_list
        # The UUID of the image. Separate multiple UUIDs with commas (,).
        self.image_uuids = image_uuids
        # The types of the assets that are scanned.
        self.scan_range = scan_range
        # The alert type of the sensitive file. Valid values:
        # 
        # *   **npm_token**: Node Package Manager (NPM) access token.
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
        # *   **esmtp_cfg**: Extended Simple Mail Transfer Protocol (ESMTP) configuration.
        # *   **docker_registry_cfg**: configuration of a Docker image repository.
        # *   **pem**: Privacy-Enhanced Mail (PEM).
        # *   **common_cred**: common credential.
        # *   **sftp_cfg**: Secure File Transfer Protocol (SFTP) connection configuration.
        # *   **grafana_token**: Grafana token.
        # *   **slack_token**: Slack token.
        # *   **ec_private_key**: Elliptic Curve (EC) private key.
        # *   **pypi_token**: upload token for the Python Package Index (PyPI).
        # *   **finicity_token**: Finicity token.
        # *   **k8s_client_key**: private key for the Kubernetes client.
        # *   **git_cfg**: Git configuration.
        # *   **django_key**: Django key.
        # *   **jenkins_ssh**: Jenkins SSH configuration file.
        # *   **openssh_private_key**: OpenSSL private key.
        # *   **square_oauth**: OAuth credential for Square.
        # *   **typeform_token**: Typeform token.
        # *   **common_database_cfg**: general database connection configuration.
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
        # *   **rails_carrierwave**: file upload credential for Rails Carrierwave.
        # *   **dbeaver_database_cfg**: DBeaver database configuration.
        # *   **robomongo_cred**: RoboMongo credential.
        # *   **github_oauth_token**: OAuth access token for GitHub.
        # *   **pulumi_token**: Pulumi token.
        # *   **ventrilo_voip**: Ventrilo VoIP server configuration.
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
        # *   **pkcs_private_key**: PKCS#12 key.
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
        # *   **heroku_api_key**: Heroku API key.
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
        # *   **lob_api_key**: Lob API key.
        # *   **pkcs_cred**: PKCS#12 certificate.
        # *   **otr_private_key**: Off-the-Record Messaging (OTR) private key.
        # *   **contentful_delivery_token**: Contentful delivery token.
        # *   **digital_ocean_tugboat**: DigitalOcean Tugboat configuration.
        # *   **dsa_private_key**: Digital Signature Algorithm (DSA) private key.
        # *   **rails_app_token**: Rails app token.
        # *   **git_cred**: Git user credential.
        # *   **newrelic_api_key**: User API key for New Relic.
        # *   **github_hub**: hub configuration for storing GitHub tokens.
        # *   **rubygem**: RubyGem token.
        self.sensitive_file_key = sensitive_file_key
        # The status of the sensitive file. Valid values:
        # 
        # *   **0**: The sensitive file is not handled.
        # *   **1**: The sensitive file is added to a whitelist.
        # *   **2**: The sensitive file is reported by mistake.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id_list is not None:
            result['IdList'] = self.id_list

        if self.image_uuids is not None:
            result['ImageUuids'] = self.image_uuids

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.sensitive_file_key is not None:
            result['SensitiveFileKey'] = self.sensitive_file_key

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')

        if m.get('ImageUuids') is not None:
            self.image_uuids = m.get('ImageUuids')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('SensitiveFileKey') is not None:
            self.sensitive_file_key = m.get('SensitiveFileKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

