# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeHanaInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        hanas: main_models.DescribeHanaInstancesResponseBodyHanas = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The information about the SAP HANA instances.
        self.hanas = hanas
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.hanas:
            self.hanas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.hanas is not None:
            result['Hanas'] = self.hanas.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Hanas') is not None:
            temp_model = main_models.DescribeHanaInstancesResponseBodyHanas()
            self.hanas = temp_model.from_map(m.get('Hanas'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHanaInstancesResponseBodyHanas(DaraModel):
    def __init__(
        self,
        hana: List[main_models.DescribeHanaInstancesResponseBodyHanasHana] = None,
    ):
        self.hana = hana

    def validate(self):
        if self.hana:
            for v1 in self.hana:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hana'] = []
        if self.hana is not None:
            for k1 in self.hana:
                result['Hana'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hana = []
        if m.get('Hana') is not None:
            for k1 in m.get('Hana'):
                temp_model = main_models.DescribeHanaInstancesResponseBodyHanasHana()
                self.hana.append(temp_model.from_map(k1))

        return self

class DescribeHanaInstancesResponseBodyHanasHana(DaraModel):
    def __init__(
        self,
        alert_setting: str = None,
        cluster_id: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        hana_name: str = None,
        host: str = None,
        instance_number: int = None,
        resource_group_id: str = None,
        status: int = None,
        status_message: str = None,
        tags: main_models.DescribeHanaInstancesResponseBodyHanasHanaTags = None,
        use_ssl: bool = None,
        user_name: str = None,
        validate_certificate: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the Cloud Backup client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   **SELF_ACCOUNT**: Data is backed up within the same Alibaba Cloud account.
        # *   **CROSS_ACCOUNT**: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The name of the SAP HANA instance.
        self.hana_name = hana_name
        # The private or internal IP address of the host where the primary node of the SAP HANA instance resides.
        self.host = host
        # The instance number of the SAP HANA system.
        self.instance_number = instance_number
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the SAP HANA instance. Valid values:
        # 
        # *   INITIALIZING: The instance is being initialized.
        # *   INITIALIZED: The instance is registered.
        # *   INVALID_HANA_NODE: The instance is invalid.
        # *   INITIALIZE_FAILED: The client fails to be installed on the instance.
        self.status = status
        # The status information.
        self.status_message = status_message
        # The tags of the SAP HANA instance.
        self.tags = tags
        # Indicates whether the SAP HANA instance is connected over Secure Sockets Layer (SSL). Valid values:
        # 
        # *   true: The SAP HANA instance is connected over SSL.
        # *   false: The SAP HANA instance is not connected over SSL.
        self.use_ssl = use_ssl
        # The username of the SYSTEMDB database.
        self.user_name = user_name
        # Indicates whether the SSL certificate of the SAP HANA instance is verified.
        self.validate_certificate = validate_certificate
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.hana_name is not None:
            result['HanaName'] = self.hana_name

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.validate_certificate is not None:
            result['ValidateCertificate'] = self.validate_certificate

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('HanaName') is not None:
            self.hana_name = m.get('HanaName')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeHanaInstancesResponseBodyHanasHanaTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('ValidateCertificate') is not None:
            self.validate_certificate = m.get('ValidateCertificate')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class DescribeHanaInstancesResponseBodyHanasHanaTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeHanaInstancesResponseBodyHanasHanaTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeHanaInstancesResponseBodyHanasHanaTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeHanaInstancesResponseBodyHanasHanaTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

