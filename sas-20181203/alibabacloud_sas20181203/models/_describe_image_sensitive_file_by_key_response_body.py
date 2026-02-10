# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageSensitiveFileByKeyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_info: main_models.DescribeImageSensitiveFileByKeyResponseBodyPageInfo = None,
        request_id: str = None,
        sensitive_file_list: List[main_models.DescribeImageSensitiveFileByKeyResponseBodySensitiveFileList] = None,
        success: bool = None,
    ):
        # The status code returned. If the 200 status code is returned, the request was successful.
        self.code = code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The information about the sensitive files.
        self.sensitive_file_list = sensitive_file_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.sensitive_file_list:
            for v1 in self.sensitive_file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SensitiveFileList'] = []
        if self.sensitive_file_list is not None:
            for k1 in self.sensitive_file_list:
                result['SensitiveFileList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageSensitiveFileByKeyResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sensitive_file_list = []
        if m.get('SensitiveFileList') is not None:
            for k1 in m.get('SensitiveFileList'):
                temp_model = main_models.DescribeImageSensitiveFileByKeyResponseBodySensitiveFileList()
                self.sensitive_file_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeImageSensitiveFileByKeyResponseBodySensitiveFileList(DaraModel):
    def __init__(
        self,
        advice: str = None,
        description: str = None,
        file_path: str = None,
        first_scan_time: int = None,
        last_scan_time: int = None,
        layer_digest: str = None,
        md_5: str = None,
        promt: str = None,
        risk_level: str = None,
        sensitive_file_key: str = None,
        sensitive_file_name: str = None,
    ):
        # The suggestion.
        self.advice = advice
        # The description of the sensitive file.
        self.description = description
        # The file path.
        self.file_path = file_path
        # The timestamp generated when the first scan was performed. Unit: milliseconds.
        self.first_scan_time = first_scan_time
        # The timestamp when the last scan was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The digest of the image.
        self.layer_digest = layer_digest
        # The MD5 value of the sensitive file.
        self.md_5 = md_5
        # The sensitive content.
        self.promt = promt
        # The risk level. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level
        # The type of the alert for the sensitive file. Valid values:
        # 
        # *   **npm_token**: NPM access token
        # *   **ftp_cfg**: FTP configuration
        # *   **google_oauth_key**: Google OAuth key
        # *   **planetscale_passwd**: PlanetScale password
        # *   **github_ssh_key**: Github SSH key
        # *   **msbuild_publish_profile**: MSBuild publish profile
        # *   **fastly_cdn_token**: Fastly CDN token
        # *   **ssh_private_key**: SSH private key
        # *   **aws_cli**: Amazon Web Services (AWS) CLI credential
        # *   **cpanel_proftpd**: cPanel ProFTPD credential
        # *   **postgresql_passwd**: PostgreSQL password file
        # *   **discord_client_cred**: Discord client credential
        # *   **rails_database**: Rails database configuration
        # *   **aws_access_key**: AWS Access Key
        # *   **esmtp_cfg**: Extended Simple Mail Transfer Protocol (ESMTP) configuration
        # *   **docker_registry_cfg**: configuration of a Docker image repository
        # *   **pem**: Privacy-Enhanced Mail (PEM)
        # *   **common_cred**: common credential
        # *   **sftp_cfg**: configuration of connection over Secure File Transfer Protocol (SFTP)
        # *   **grafana_token**: Grafana token
        # *   **slack_token**: Slack token
        # *   **ec_private_key**: Elliptic Curve (EC) private key
        # *   **pypi_token**: Python Package Index (PyPI) token
        # *   **finicity_token**: Finicity token
        # *   **k8s_client_key**: private key for the Kubernetes client
        # *   **git_cfg**: Git configuration
        # *   **django_key**: Django key
        # *   **jenkins_ssh**: SSH configuration file for Jenkins
        # *   **openssh_private_key**: OpenSSH private key
        # *   **square_oauth**: Square OAuth credential
        # *   **typeform_token**: Typeform token
        # *   **common_database_cfg**: configuration of general database connection
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
        # *   **robomongo_cred**: RoboMongo credential
        # *   **github_oauth_token**: OAuth access token for GitHub
        # *   **pulumi_token**: Pulumi token
        # *   **ventrilo_voip**: configuration of a Ventrilo VoIP server
        # *   **macos_keychain**: macOS Keychain
        # *   **amazon_mws_token**: Amazon MWS token
        # *   **dynatrace_token**: Dynatrace token
        # *   **java_keystore**: Java KeyStore (JKS)
        # *   **microsoft_sdf**: Microsoft SQL Server Compact Edition (CE) database
        # *   **kubernetes_dashboard_cred**: user credential for Kubernetes Dashboard
        # *   **atlassian_token**: Atlassian token
        # *   **rdp**: remote desktop protocol (RDP)
        # *   **mailgun_key**: Mailgun webhook signing key
        # *   **mailchimp_api_key**: API key for Mailchimp
        # *   **netrc_cfg**: netrc configuration file
        # *   **openvpn_cfg**: configuration of the OpenVPN client
        # *   **github_refresh_token**: GitHub refresh token
        # *   **salesforce**: Salesforce credential
        # *   **salesforce**: Sendinblue token
        # *   **pkcs_private_key**: PKCS#12 private key
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
        # *   **heroku_api_key**: API key for Heroku
        # *   **messagebird_token**: MessageBird token
        # *   **github_app_token**: Github app token
        # *   **hashicorp_vault_token**: HashiCorp Vault token
        # *   **pgp_private_key**: PGP private key
        # *   **sshpasswd**: SSH password
        # *   **huaweicloud_ak**: secret access key of a third-party cloud
        # *   **aws_s3cmd**: AWS S3cmd configuration
        # *   **php_config**: PHP configuration
        # *   **common_private_key**: common private key
        # *   **microsoft_mdf**: Microsoft SQL Server database
        # *   **mediawiki_cfg**: MediaWiki configuration
        # *   **jenkins_cred**: Jenkins credential
        # *   **rubygems_cred**: RubyGems credential
        # *   **clojars_token**: Clojars token
        # *   **phoenix_web_passwd**: Phoenix web credential
        # *   **puttygen_private_key**: PuTTYgen private key
        # *   **google_oauth_token**: Google OAuth access token
        # *   **rubyonrails_cfg**: Ruby On Rails database configuration
        # *   **lob_api_key**: Lob API key for Lob
        # *   **pkcs_cred**: PKCS#12 certificate
        # *   **otr_private_key**: Off-the-Record Messaging (OTR) private key
        # *   **contentful_delivery_token**: Contentful delivery token
        # *   **digital_ocean_tugboat**: DigitalOcean Tugboat configuration
        # *   **dsa_private_key**: Digital Signature Algorithm (DSA) private key
        # *   **rails_app_token**: app token for Rails
        # *   **git_cred**: Git user credential
        # *   **newrelic_api_key**: User API key for New Relic
        # *   **github_hub**: hub configuration for storing GitHub tokens
        # *   **rubygem**: Rubygem Token
        self.sensitive_file_key = sensitive_file_key
        # The name of the alert type for the sensitive file.
        self.sensitive_file_name = sensitive_file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice is not None:
            result['Advice'] = self.advice

        if self.description is not None:
            result['Description'] = self.description

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.layer_digest is not None:
            result['LayerDigest'] = self.layer_digest

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.promt is not None:
            result['Promt'] = self.promt

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sensitive_file_key is not None:
            result['SensitiveFileKey'] = self.sensitive_file_key

        if self.sensitive_file_name is not None:
            result['SensitiveFileName'] = self.sensitive_file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('LayerDigest') is not None:
            self.layer_digest = m.get('LayerDigest')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Promt') is not None:
            self.promt = m.get('Promt')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SensitiveFileKey') is not None:
            self.sensitive_file_key = m.get('SensitiveFileKey')

        if m.get('SensitiveFileName') is not None:
            self.sensitive_file_name = m.get('SensitiveFileName')

        return self

class DescribeImageSensitiveFileByKeyResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        last_row_key: str = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The key of the last data entry.
        self.last_row_key = last_row_key
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.last_row_key is not None:
            result['LastRowKey'] = self.last_row_key

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('LastRowKey') is not None:
            self.last_row_key = m.get('LastRowKey')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

