# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageSensitiveFileListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_info: main_models.DescribeImageSensitiveFileListResponseBodyPageInfo = None,
        request_id: str = None,
        sensitive_file_list: List[main_models.DescribeImageSensitiveFileListResponseBodySensitiveFileList] = None,
        success: bool = None,
    ):
        # The result code. A value of **200** indicates success. Other values indicate failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The detailed information about the error code.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The ID of the request. Alibaba Cloud generates a unique ID for each request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The list of sensitive files.
        self.sensitive_file_list = sensitive_file_list
        # Indicates whether the query was successful. Valid values:
        # - **true**: successful
        # - **false**: failed.
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
            temp_model = main_models.DescribeImageSensitiveFileListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sensitive_file_list = []
        if m.get('SensitiveFileList') is not None:
            for k1 in m.get('SensitiveFileList'):
                temp_model = main_models.DescribeImageSensitiveFileListResponseBodySensitiveFileList()
                self.sensitive_file_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeImageSensitiveFileListResponseBodySensitiveFileList(DaraModel):
    def __init__(
        self,
        advice: str = None,
        class_key: str = None,
        class_name: str = None,
        count: int = None,
        description: str = None,
        first_scan_time: int = None,
        last_scan_time: int = None,
        risk_level: str = None,
        sensitive_file_key: str = None,
        sensitive_file_name: str = None,
        status: int = None,
        unprocessed_num: int = None,
    ):
        # The hardening suggestion for the sensitive file check item.
        self.advice = advice
        # The classification key of the sensitive file.
        self.class_key = class_key
        # The classification name of the sensitive file.
        self.class_name = class_name
        # The number of times the sensitive file was detected by scans.
        self.count = count
        # The description of the sensitive file check item.
        self.description = description
        # The timestamp of the first scan. Unit: milliseconds.
        self.first_scan_time = first_scan_time
        # The timestamp of the most recent scan. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The risk level. Valid values:
        # 
        # - **high**: high
        # 
        # - **medium**: medium
        # 
        # - **low**: low.
        self.risk_level = risk_level
        # The sensitive file alerting type. Valid values:
        # 
        # - **npm_token**: NPM access token
        # - **ftp_cfg**: FTP configuration
        # - **google_oauth_key**: Google OAuth Key
        # - **planetscale_passwd**: Planetscale password
        # - **github_ssh_key**: Github SSH key
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
        # - **docker_registry_cfg**: Docker image repository configuration
        # - **pem**: PEM
        # - **common_cred**: common credentials
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
        # - **openssh_private_key**: OPENSSH private key
        # - **square_oauth**: Square OAuth credentials
        # - **typeform_token**: Typeform token
        # - **common_database_cfg**: common database connection configuration
        # - **wordpress_database_cfg**: WordPress database configuration
        # - **googlecloud_api_key**: Google Cloud API Key
        # - **vscode_sftp**: VSCode SFTP configuration
        # - **apache_htpasswd**: Apache htpasswd
        # - **planetscale_token**: Planetscale token
        # - **contentful_preview_token**: Contentful Preview token
        # - **php_database_cfg**: PHP application database password
        # - **atom_remote_sync**: Atom remote synchronization configuration
        # - **aws_session_token**: AWS session token
        # - **atom_sftp_cfg**: Atom SFTP configuration
        # - **asana_client_private_key**: Asana client private key
        # - **tencentcloud_ak**: third-party cloud SecretId
        # - **rsa_private_key**: RSA private key
        # - **github_personal_token**: Github Personal access token
        # - **pgp**: PGP encrypt file
        # - **stripe_skpk**: Stripe Secret Key
        # - **square_token**: Square access token
        # - **rails_carrierwave**: Rails Carrierwave file upload credentials
        # - **dbeaver_database_cfg**: DBeaver database configuration
        # - **robomongo_cred**: Robomongo credentials
        # - **github_oauth_token**: Github OAuth access token
        # - **pulumi_token**: Pulumi token
        # - **ventrilo_voip**: Ventrilo VoIP Server configuration
        # - **macos_keychain**: macOS Keychain
        # - **amazon_mws_token**: Amazon MWS Token
        # - **dynatrace_token**: Dynatrace token
        # - **java_keystore**: Java KeyStore
        # - **microsoft_sdf**: Microsoft SQL CE database
        # - **kubernetes_dashboard_cred**: Kubernetes Dashboard user credentials
        # - **atlassian_token**: Atlassian token
        # - **rdp**: Remote Desktop Protocol (RDP) connection
        # - **mailgun_key**: Mailgun Webhook Signing Key
        # - **mailchimp_api_key**: Mailchimp API Key
        # - **netrc_cfg**: .netrc configuration file
        # - **openvpn_cfg**: OpenVPN client configuration
        # - **github_refresh_token**: Github Refresh Token
        # - **salesforce**: Salesforce credentials
        # - **sendinblue**: Sendinblue token
        # - **pkcs_private_key**: PKCS#12 key
        # - **rubyonrails_passwd**: Ruby on Rails password file
        # - **filezilla_ftp**: FileZilla FTP configuration
        # - **databricks_token**: Databricks token
        # - **gitLab_personal_token**: GitLab Personal access token
        # - **rails_master_key**: Rails Master Key
        # - **sqlite**: SQLite3/SQLite database
        # - **firefox_logins**: Firefox logon configuration
        # - **mailgun_private_token**: Mailgun Private token
        # - **joomla_cfg**: Joomla configuration
        # - **hashicorp_terraform_token**: Hashicorp Terraform Token
        # - **jetbrains_ides**: Jetbrains IDEs configuration
        # - **heroku_api_key**: Heroku API key
        # - **messagebird_token**: MessageBird token
        # - **github_app_token**: Github App Token
        # - **hashicorp_vault_token**: Hashicorp Vault Token
        # - **pgp_private_key**: PGP private key
        # - **sshpasswd**: SSH password
        # - **huaweicloud_ak**: third-party cloud Secret Access Key
        # - **aws_s3cmd**: AWS S3cmd configuration
        # - **php_config**: PHP configuration
        # - **common_private_key**: common private key types
        # - **microsoft_mdf**: Microsoft SQL database
        # - **mediawiki_cfg**: MediaWiki configuration
        # - **jenkins_cred**: Jenkins credentials
        # - **rubygems_cred**: Rubygems credentials
        # - **clojars_token**: Clojars token
        # - **phoenix_web_passwd**: Phoenix Web credentials
        # - **puttygen_private_key**: PuTTYgen private key
        # - **google_oauth_token**: Google OAuth access token
        # - **rubyonrails_cfg**: Ruby On Rails database configuration
        # - **lob_api_key**: Lob API Key
        # - **pkcs_cred**: PKCS#12 certificate
        # - **otr_private_key**: OTR private key
        # - **contentful_delivery_token**: Contentful Delivery token
        # - **digital_ocean_tugboat**: Digital Ocean Tugboat configuration
        # - **dsa_private_key**: DSA private key
        # - **rails_app_token**: Rails App token
        # - **git_cred**: Git user credentials
        # - **newrelic_api_key**: New Relic User API Key
        # - **github_hub**: hub configuration that stores Github tokens
        # - **rubygem**: Rubygem token.
        self.sensitive_file_key = sensitive_file_key
        # The name of the sensitive file alerting type.
        self.sensitive_file_name = sensitive_file_name
        # The status of the sensitive file check item. Valid values:
        # - **0**: Unprocessed.
        # - **1**: Processed.
        self.status = status
        # The number of unprocessed images.
        self.unprocessed_num = unprocessed_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice is not None:
            result['Advice'] = self.advice

        if self.class_key is not None:
            result['ClassKey'] = self.class_key

        if self.class_name is not None:
            result['ClassName'] = self.class_name

        if self.count is not None:
            result['Count'] = self.count

        if self.description is not None:
            result['Description'] = self.description

        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sensitive_file_key is not None:
            result['SensitiveFileKey'] = self.sensitive_file_key

        if self.sensitive_file_name is not None:
            result['SensitiveFileName'] = self.sensitive_file_name

        if self.status is not None:
            result['Status'] = self.status

        if self.unprocessed_num is not None:
            result['UnprocessedNum'] = self.unprocessed_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')

        if m.get('ClassKey') is not None:
            self.class_key = m.get('ClassKey')

        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SensitiveFileKey') is not None:
            self.sensitive_file_key = m.get('SensitiveFileKey')

        if m.get('SensitiveFileName') is not None:
            self.sensitive_file_name = m.get('SensitiveFileName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnprocessedNum') is not None:
            self.unprocessed_num = m.get('UnprocessedNum')

        return self

class DescribeImageSensitiveFileListResponseBodyPageInfo(DaraModel):
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
        # The page number of the current page in a paging query.
        self.current_page = current_page
        # The key of the last entry.
        self.last_row_key = last_row_key
        # The number of entries returned per page. Default value: 20.
        self.page_size = page_size
        # The total number of entries.
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

