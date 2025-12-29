# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        data: main_models.ListApplicationsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        # The HTTP status code. Take note of the following rules:
        # 
        # - **2xx**: The call was successful.
        # - **3xx**: The call was redirected.
        # - **4xx**: The call failed.
        # - **5xx**: A server error occurred.
        self.code = code
        # The current page number.
        self.current_page = current_page
        # The queried applications.
        self.data = data
        # The returned error code. Valid values:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the "**Error codes**" section of this topic.
        self.error_code = error_code
        # Additional message.
        self.message = message
        # The page size.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The number of applications.
        self.total_size = total_size

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Data') is not None:
            temp_model = main_models.ListApplicationsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListApplicationsResponseBodyData(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListApplicationsResponseBodyDataApplications] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The queried applications.
        self.applications = applications
        # The current page number.
        self.current_page = current_page
        # The number of records in each page.
        self.page_size = page_size
        # The number of applications.
        self.total_size = total_size

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListApplicationsResponseBodyDataApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListApplicationsResponseBodyDataApplications(DaraModel):
    def __init__(
        self,
        app_deleting_status: bool = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        base_app_id: str = None,
        children: List[main_models.ListApplicationsResponseBodyDataApplicationsChildren] = None,
        cpu: int = None,
        disk_size: int = None,
        enable_idle: str = None,
        image_url: str = None,
        instances: int = None,
        is_stateful: bool = None,
        mem: int = None,
        mse_enabled: bool = None,
        mse_namespace_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        new_sae_version: str = None,
        package_url: str = None,
        programming_language: str = None,
        region_id: str = None,
        resource_type: str = None,
        running_instances: int = None,
        tags: List[main_models.ListApplicationsResponseBodyDataApplicationsTags] = None,
        vpc_id: str = None,
    ):
        # Indicates whether the application is being deleted. Valid values:
        # 
        # *   **true**: The application is being deleted.
        # *   **false**: The application is not being deleted.
        self.app_deleting_status = app_deleting_status
        # The description of the application.
        self.app_description = app_description
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The application type.
        self.app_type = app_type
        # The base app ID. Only gray-release applications have this property.
        self.base_app_id = base_app_id
        # The gray-release application list of this application.
        self.children = children
        # The CPU specifications that are required for each instance. Unit: millicores. This parameter cannot be set to 0. Valid values:
        # 
        # *   **500**
        # *   **1000**
        # *   **2000**
        # *   **4000**
        # *   **8000**
        # *   **16000**
        # *   **32000**
        self.cpu = cpu
        # The disk size. Unit: GB.
        self.disk_size = disk_size
        # If the idle mode is enabled.
        self.enable_idle = enable_idle
        # The image URL.
        self.image_url = image_url
        # The number of application instances.
        self.instances = instances
        self.is_stateful = is_stateful
        # The memory size that is required by each instance. Unit: MB. This parameter cannot be set to 0. The values of this parameter correspond to the values of the Cpu parameter:
        # 
        # *   This parameter is set to **1024** if the Cpu parameter is set to 500 or 1000.
        # *   This parameter is set to **2048** if the Cpu parameter is set to 500, 1000, or 2000.
        # *   This parameter is set to **4096** if the Cpu parameter is set to 1000, 2000, or 4000.
        # *   This parameter is set to **8192** if the Cpu parameter is set to 2000, 4000, or 8000.
        # *   This parameter is set to **12288** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **16384** if the Cpu parameter is set to 4000, 8000, or 16000.
        # *   This parameter is set to **24576** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **32768** if the Cpu parameter is set to 16000.
        # *   This parameter is set to **65536** if the Cpu parameter is set to 8000, 16000, or 32000.
        # *   This parameter is set to **131072** if the Cpu parameter is set to 32000.
        self.mem = mem
        # The application has enabled MSE or not.
        self.mse_enabled = mse_enabled
        # The name space of MSE:
        # 
        # - default: the free edition.
        # - sae-pro: the professional edition.
        # - sae-ent: the enterprise eiditon.
        self.mse_namespace_id = mse_namespace_id
        # The namespace ID.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The application edition.
        # 
        # - lite: the lightweight edition.
        # - std: the standard edition.
        # - pro: the professional edition.
        self.new_sae_version = new_sae_version
        # The package URL.
        self.package_url = package_url
        # The programming language of the application.
        self.programming_language = programming_language
        # The region ID.
        self.region_id = region_id
        self.resource_type = resource_type
        # The number of running instances.
        self.running_instances = running_instances
        # The tags of the application.
        self.tags = tags
        # VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_deleting_status is not None:
            result['AppDeletingStatus'] = self.app_deleting_status

        if self.app_description is not None:
            result['AppDescription'] = self.app_description

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.base_app_id is not None:
            result['BaseAppId'] = self.base_app_id

        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.enable_idle is not None:
            result['EnableIdle'] = self.enable_idle

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.instances is not None:
            result['Instances'] = self.instances

        if self.is_stateful is not None:
            result['IsStateful'] = self.is_stateful

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.mse_enabled is not None:
            result['MseEnabled'] = self.mse_enabled

        if self.mse_namespace_id is not None:
            result['MseNamespaceId'] = self.mse_namespace_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.new_sae_version is not None:
            result['NewSaeVersion'] = self.new_sae_version

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDeletingStatus') is not None:
            self.app_deleting_status = m.get('AppDeletingStatus')

        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BaseAppId') is not None:
            self.base_app_id = m.get('BaseAppId')

        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.ListApplicationsResponseBodyDataApplicationsChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('EnableIdle') is not None:
            self.enable_idle = m.get('EnableIdle')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        if m.get('IsStateful') is not None:
            self.is_stateful = m.get('IsStateful')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('MseEnabled') is not None:
            self.mse_enabled = m.get('MseEnabled')

        if m.get('MseNamespaceId') is not None:
            self.mse_namespace_id = m.get('MseNamespaceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NewSaeVersion') is not None:
            self.new_sae_version = m.get('NewSaeVersion')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListApplicationsResponseBodyDataApplicationsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListApplicationsResponseBodyDataApplicationsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

class ListApplicationsResponseBodyDataApplicationsChildren(DaraModel):
    def __init__(
        self,
        app_deleting_status: bool = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        base_app_id: str = None,
        cpu: int = None,
        instances: int = None,
        is_stateful: bool = None,
        mem: int = None,
        mse_enabled: bool = None,
        namespace_id: str = None,
        namespace_name: str = None,
        new_sae_version: str = None,
        programming_language: str = None,
        region_id: str = None,
        resource_type: str = None,
        running_instances: int = None,
        scale_rule_enabled: bool = None,
        scale_rule_type: str = None,
        tags: List[main_models.ListApplicationsResponseBodyDataApplicationsChildrenTags] = None,
    ):
        # If is deleting this application.
        self.app_deleting_status = app_deleting_status
        # The application description.
        self.app_description = app_description
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The way to deploy applications.
        self.app_type = app_type
        # The base application ID.
        self.base_app_id = base_app_id
        # The CPU sepcification.
        self.cpu = cpu
        # The number of instances.
        self.instances = instances
        self.is_stateful = is_stateful
        # The memory specification.
        self.mem = mem
        # If this application has enabled MSE.
        self.mse_enabled = mse_enabled
        # The namespace ID.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The application edition.
        # 
        # - lite: the lightweight edition.
        # - std: the standard edition.
        # - pro: the professional edition.
        self.new_sae_version = new_sae_version
        # The programming language of this application.
        self.programming_language = programming_language
        # The region ID.
        self.region_id = region_id
        self.resource_type = resource_type
        # The number of instances in running state.
        self.running_instances = running_instances
        # If the scale rule is enabled.
        self.scale_rule_enabled = scale_rule_enabled
        # The type of the scale rule.
        self.scale_rule_type = scale_rule_type
        # The application tag.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_deleting_status is not None:
            result['AppDeletingStatus'] = self.app_deleting_status

        if self.app_description is not None:
            result['AppDescription'] = self.app_description

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.base_app_id is not None:
            result['BaseAppId'] = self.base_app_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.instances is not None:
            result['Instances'] = self.instances

        if self.is_stateful is not None:
            result['IsStateful'] = self.is_stateful

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.mse_enabled is not None:
            result['MseEnabled'] = self.mse_enabled

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.new_sae_version is not None:
            result['NewSaeVersion'] = self.new_sae_version

        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances

        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled

        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDeletingStatus') is not None:
            self.app_deleting_status = m.get('AppDeletingStatus')

        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BaseAppId') is not None:
            self.base_app_id = m.get('BaseAppId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        if m.get('IsStateful') is not None:
            self.is_stateful = m.get('IsStateful')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('MseEnabled') is not None:
            self.mse_enabled = m.get('MseEnabled')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NewSaeVersion') is not None:
            self.new_sae_version = m.get('NewSaeVersion')

        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')

        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')

        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListApplicationsResponseBodyDataApplicationsChildrenTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListApplicationsResponseBodyDataApplicationsChildrenTags(DaraModel):
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

