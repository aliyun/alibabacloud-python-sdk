# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class ProductComponentRelationDetail(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        category: str = None,
        class_: str = None,
        component_name: str = None,
        component_orchestration_values: str = None,
        component_uid: str = None,
        component_version_uid: str = None,
        created_at: str = None,
        description: str = None,
        documents: str = None,
        enable: bool = None,
        images_mapping: str = None,
        namespace: str = None,
        orchestration_type: str = None,
        parent_component: bool = None,
        parent_component_version_relation_uid: str = None,
        parent_component_version_uid: str = None,
        priority: int = None,
        product_version_uid: str = None,
        provider: str = None,
        public: bool = None,
        readme: str = None,
        relation_uid: str = None,
        release_name: str = None,
        resources: str = None,
        sequence: int = None,
        singleton: bool = None,
        source: str = None,
        version: str = None,
    ):
        # appVersion
        self.app_version = app_version
        # category
        self.category = category
        # class
        self.class_ = class_
        # componentName
        self.component_name = component_name
        # componentOrchestrationValues
        self.component_orchestration_values = component_orchestration_values
        # componentUID
        self.component_uid = component_uid
        # componentVersionUID
        self.component_version_uid = component_version_uid
        # createdAt
        self.created_at = created_at
        # description
        self.description = description
        # documents
        self.documents = documents
        # enable
        self.enable = enable
        # imagesMapping
        self.images_mapping = images_mapping
        # namespace
        self.namespace = namespace
        # orchestrationType
        self.orchestration_type = orchestration_type
        # parentComponent
        self.parent_component = parent_component
        # parentComponentVersionRelationUID
        self.parent_component_version_relation_uid = parent_component_version_relation_uid
        # parentComponentVersionUID
        self.parent_component_version_uid = parent_component_version_uid
        # priority
        self.priority = priority
        # productVersionUID
        self.product_version_uid = product_version_uid
        # provider
        self.provider = provider
        # public
        self.public = public
        # readme
        self.readme = readme
        # relationUID
        self.relation_uid = relation_uid
        # releaseName
        self.release_name = release_name
        # resources
        self.resources = resources
        # sequence
        self.sequence = sequence
        # singleton
        self.singleton = singleton
        # source
        self.source = source
        # version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.class_ is not None:
            result['class'] = self.class_
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.enable is not None:
            result['enable'] = self.enable
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.parent_component_version_relation_uid is not None:
            result['parentComponentVersionRelationUID'] = self.parent_component_version_relation_uid
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.priority is not None:
            result['priority'] = self.priority
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.readme is not None:
            result['readme'] = self.readme
        if self.relation_uid is not None:
            result['relationUID'] = self.relation_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.resources is not None:
            result['resources'] = self.resources
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('parentComponentVersionRelationUID') is not None:
            self.parent_component_version_relation_uid = m.get('parentComponentVersionRelationUID')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('relationUID') is not None:
            self.relation_uid = m.get('relationUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class FoundationVersionPlatforms(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        # architecture
        self.architecture = architecture
        # os
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class FoundationVersion(TeaModel):
    def __init__(
        self,
        description: str = None,
        documents: str = None,
        name: str = None,
        platforms: FoundationVersionPlatforms = None,
        status: str = None,
        uid: str = None,
        version: str = None,
    ):
        # description
        self.description = description
        # documents
        self.documents = documents
        # name
        self.name = name
        # platforms
        self.platforms = platforms
        # status
        self.status = status
        # uid
        self.uid = uid
        # version
        self.version = version

    def validate(self):
        if self.platforms:
            self.platforms.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.platforms is not None:
            result['platforms'] = self.platforms.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platforms') is not None:
            temp_model = FoundationVersionPlatforms()
            self.platforms = temp_model.from_map(m['platforms'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Platform(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        # architecture
        self.architecture = architecture
        # os
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ComponentVersion(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        component_name: str = None,
        component_uid: str = None,
        description: str = None,
        documents: str = None,
        images_mapping: str = None,
        namespace: str = None,
        orchestration_type: str = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        platforms: List[Platform] = None,
        readme: str = None,
        resources: str = None,
        source: str = None,
        uid: str = None,
        version: str = None,
    ):
        # appVersion
        self.app_version = app_version
        # componentName
        self.component_name = component_name
        # componentUID
        self.component_uid = component_uid
        # description
        self.description = description
        # documents
        self.documents = documents
        # imagesMapping
        self.images_mapping = images_mapping
        # namespace
        self.namespace = namespace
        # orchestrationType
        self.orchestration_type = orchestration_type
        # orchestrationValues
        self.orchestration_values = orchestration_values
        # packageURL
        self.package_url = package_url
        # parentComponent
        self.parent_component = parent_component
        # platforms
        self.platforms = platforms
        # readme
        self.readme = readme
        # resources
        self.resources = resources
        # source
        self.source = source
        # uid
        self.uid = uid
        # version
        self.version = version

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetEnvironmentResponseBodyDataPlatform(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class GetEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        created_at: str = None,
        description: str = None,
        instance_list: str = None,
        location: str = None,
        name: str = None,
        platform: GetEnvironmentResponseBodyDataPlatform = None,
        product_name: str = None,
        product_version: str = None,
        uid: str = None,
        vendor_config: str = None,
        vendor_type: str = None,
        instance_status: str = None,
    ):
        self.cluster_id = cluster_id
        self.created_at = created_at
        self.description = description
        self.instance_list = instance_list
        self.location = location
        self.name = name
        self.platform = platform
        self.product_name = product_name
        self.product_version = product_version
        self.uid = uid
        self.vendor_config = vendor_config
        self.vendor_type = vendor_type
        self.instance_status = instance_status

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = GetEnvironmentResponseBodyDataPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        return self


class GetEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        data: GetEnvironmentResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionRelatedComponentVersionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ProductComponentRelationDetail] = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ProductComponentRelationDetail()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListProductVersionRelatedComponentVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProductVersionRelatedComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProductVersionRelatedComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComponentVersionChildrenResponseBodyData(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        component_uid: str = None,
        description: str = None,
        documents: List[str] = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        product_component_version_uid: str = None,
        provider: str = None,
        readme: str = None,
        resources: str = None,
        uid: str = None,
        version: str = None,
    ):
        self.component_name = component_name
        self.component_uid = component_uid
        self.description = description
        self.documents = documents
        self.orchestration_values = orchestration_values
        self.package_url = package_url
        self.parent_component = parent_component
        self.product_component_version_uid = product_component_version_uid
        self.provider = provider
        self.readme = readme
        self.resources = resources
        self.uid = uid
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.product_component_version_uid is not None:
            result['productComponentVersionUID'] = self.product_component_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('productComponentVersionUID') is not None:
            self.product_component_version_uid = m.get('productComponentVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetComponentVersionChildrenResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetComponentVersionChildrenResponseBodyData] = None,
        err_code: str = None,
        err_msg: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetComponentVersionChildrenResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetComponentVersionChildrenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetComponentVersionChildrenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetComponentVersionChildrenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        cluster_uid: str = None,
        description: str = None,
        instance_list: str = None,
        instance_status: str = None,
        name: str = None,
        product_name: str = None,
        product_version: str = None,
        type: str = None,
        uid: str = None,
        vendor_config: str = None,
        vendor_type: str = None,
    ):
        self.created_at = created_at
        self.cluster_uid = cluster_uid
        self.description = description
        self.instance_list = instance_list
        self.instance_status = instance_status
        self.name = name
        self.product_name = product_name
        self.product_version = product_version
        self.type = type
        self.uid = uid
        self.vendor_config = vendor_config
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.cluster_uid is not None:
            result['clusterUID'] = self.cluster_uid
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('clusterUID') is not None:
            self.cluster_uid = m.get('clusterUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetProductEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        data: GetProductEnvironmentResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionPackageRequest(TeaModel):
    def __init__(
        self,
        platform: str = None,
        package_type: str = None,
        old_product_version_uid: str = None,
    ):
        self.platform = platform
        self.package_type = package_type
        self.old_product_version_uid = old_product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.platform is not None:
            result['platform'] = self.platform
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        return self


class GetProductVersionPackageResponseBodyData(TeaModel):
    def __init__(
        self,
        package_url: str = None,
    ):
        self.package_url = package_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        return self


class GetProductVersionPackageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetProductVersionPackageResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductVersionPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductVersionPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductVersionPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductVersionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlicloudRegionResponseBodyDataRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAlicloudRegionResponseBodyDataRegions(TeaModel):
    def __init__(
        self,
        region: List[ListAlicloudRegionResponseBodyDataRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = ListAlicloudRegionResponseBodyDataRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class ListAlicloudRegionResponseBodyData(TeaModel):
    def __init__(
        self,
        regions: ListAlicloudRegionResponseBodyDataRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = ListAlicloudRegionResponseBodyDataRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAlicloudRegionResponseBody(TeaModel):
    def __init__(
        self,
        data: ListAlicloudRegionResponseBodyData = None,
        success: bool = None,
    ):
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListAlicloudRegionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListAlicloudRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlicloudRegionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlicloudRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentVersionsRequestPlatforms(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListComponentVersionsRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        platforms: List[ListComponentVersionsRequestPlatforms] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.platforms = platforms

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListComponentVersionsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        return self


class ListComponentVersionsShrinkRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        platforms_shrink: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.platforms_shrink = platforms_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        return self


class ListComponentVersionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        component_name: str = None,
        component_uid: str = None,
        description: str = None,
        documents: str = None,
        images_mapping: str = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        provider: str = None,
        readme: str = None,
        resources: str = None,
        uid: str = None,
        version: str = None,
    ):
        self.app_version = app_version
        self.component_name = component_name
        self.component_uid = component_uid
        self.description = description
        self.documents = documents
        self.images_mapping = images_mapping
        self.orchestration_values = orchestration_values
        self.package_url = package_url
        self.parent_component = parent_component
        self.provider = provider
        self.readme = readme
        self.resources = resources
        self.uid = uid
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListComponentVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListComponentVersionsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListComponentVersionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListComponentVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListComponentVersionsResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = ListComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListComponentVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotInstanceJoinOptionWithBatchRequest(TeaModel):
    def __init__(
        self,
        instance_uids: str = None,
        join_snapshot: bool = None,
        root_password: str = None,
    ):
        self.instance_uids = instance_uids
        self.join_snapshot = join_snapshot
        self.root_password = root_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_uids is not None:
            result['instanceUIDs'] = self.instance_uids
        if self.join_snapshot is not None:
            result['joinSnapshot'] = self.join_snapshot
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceUIDs') is not None:
            self.instance_uids = m.get('instanceUIDs')
        if m.get('joinSnapshot') is not None:
            self.join_snapshot = m.get('joinSnapshot')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        return self


class UpdateSnapshotInstanceJoinOptionWithBatchResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateSnapshotInstanceJoinOptionWithBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSnapshotInstanceJoinOptionWithBatchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSnapshotInstanceJoinOptionWithBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVendorConfigTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        vendor_config: str = None,
    ):
        self.vendor_config = vendor_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class GenerateVendorConfigTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateVendorConfigTemplateResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GenerateVendorConfigTemplateResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GenerateVendorConfigTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateVendorConfigTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateVendorConfigTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductComponentRequest(TeaModel):
    def __init__(
        self,
        component_orchestration_values: str = None,
        enable: bool = None,
        release_name: str = None,
    ):
        self.component_orchestration_values = component_orchestration_values
        self.enable = enable
        self.release_name = release_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.enable is not None:
            result['enable'] = self.enable
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        return self


class UpdateProductComponentResponseBody(TeaModel):
    def __init__(
        self,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProductComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProductComponentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProductComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentNodesRequestDataDisk2(TeaModel):
    def __init__(
        self,
        name: str = None,
        size: str = None,
    ):
        self.name = name
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class UpdateEnvironmentNodesRequestSystemDisk2(TeaModel):
    def __init__(
        self,
        name: str = None,
        size: str = None,
    ):
        self.name = name
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class UpdateEnvironmentNodesRequestTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        self.effect = effect
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateEnvironmentNodesRequest(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        data_disk: List[str] = None,
        data_disk_2: List[UpdateEnvironmentNodesRequestDataDisk2] = None,
        env_uid: str = None,
        identifier: str = None,
        labels: Dict[str, Any] = None,
        memory: int = None,
        node_ip: str = None,
        root_password: str = None,
        system_disk: List[str] = None,
        system_disk_2: List[UpdateEnvironmentNodesRequestSystemDisk2] = None,
        taints: List[UpdateEnvironmentNodesRequestTaints] = None,
    ):
        self.cpu = cpu
        self.data_disk = data_disk
        self.data_disk_2 = data_disk_2
        self.env_uid = env_uid
        self.identifier = identifier
        self.labels = labels
        self.memory = memory
        self.node_ip = node_ip
        self.root_password = root_password
        self.system_disk = system_disk
        self.system_disk_2 = system_disk_2
        self.taints = taints

    def validate(self):
        if self.data_disk_2:
            for k in self.data_disk_2:
                if k:
                    k.validate()
        if self.system_disk_2:
            for k in self.system_disk_2:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.data_disk is not None:
            result['dataDisk'] = self.data_disk
        result['dataDisk2'] = []
        if self.data_disk_2 is not None:
            for k in self.data_disk_2:
                result['dataDisk2'].append(k.to_map() if k else None)
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.labels is not None:
            result['labels'] = self.labels
        if self.memory is not None:
            result['memory'] = self.memory
        if self.node_ip is not None:
            result['nodeIP'] = self.node_ip
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        if self.system_disk is not None:
            result['systemDisk'] = self.system_disk
        result['systemDisk2'] = []
        if self.system_disk_2 is not None:
            for k in self.system_disk_2:
                result['systemDisk2'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('dataDisk') is not None:
            self.data_disk = m.get('dataDisk')
        self.data_disk_2 = []
        if m.get('dataDisk2') is not None:
            for k in m.get('dataDisk2'):
                temp_model = UpdateEnvironmentNodesRequestDataDisk2()
                self.data_disk_2.append(temp_model.from_map(k))
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('nodeIP') is not None:
            self.node_ip = m.get('nodeIP')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        if m.get('systemDisk') is not None:
            self.system_disk = m.get('systemDisk')
        self.system_disk_2 = []
        if m.get('systemDisk2') is not None:
            for k in m.get('systemDisk2'):
                temp_model = UpdateEnvironmentNodesRequestSystemDisk2()
                self.system_disk_2.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = UpdateEnvironmentNodesRequestTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class UpdateEnvironmentNodesResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateEnvironmentNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEnvironmentNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentPackagesRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnvironmentPackagesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        env_uid: str = None,
        provider: str = None,
        status: str = None,
        uid: str = None,
        url: str = None,
    ):
        self.env_uid = env_uid
        self.provider = provider
        self.status = status
        self.uid = uid
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEnvironmentPackagesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListEnvironmentPackagesResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentPackagesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentPackagesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEnvironmentPackagesResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentPackagesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEnvironmentPackagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateEnvironmentRequestPlatform(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class CreateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        annotations: str = None,
        description: str = None,
        location: str = None,
        name: str = None,
        platform: CreateEnvironmentRequestPlatform = None,
        vendor_type: str = None,
    ):
        self.annotations = annotations
        self.description = description
        self.location = location
        self.name = name
        self.platform = platform
        self.vendor_type = vendor_type

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.description is not None:
            result['description'] = self.description
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = CreateEnvironmentRequestPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class CreateEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateEnvironmentResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentLogResponseBodyData(TeaModel):
    def __init__(
        self,
        end: bool = None,
        message: str = None,
    ):
        self.end = end
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetEnvironmentLogResponseBody(TeaModel):
    def __init__(
        self,
        data: GetEnvironmentLogResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEnvironmentLogResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnvironmentLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEnvironmentLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentNodeRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        name: str = None,
        fuzzy: str = None,
        node_ip: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.name = name
        self.fuzzy = fuzzy
        self.node_ip = node_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.name is not None:
            result['name'] = self.name
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.node_ip is not None:
            result['nodeIp'] = self.node_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('nodeIp') is not None:
            self.node_ip = m.get('nodeIp')
        return self


class ListEnvironmentNodeResponseBodyDataList(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        product_name: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        uid: str = None,
        vendor_type: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.uid = uid
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentNodeResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListEnvironmentNodeResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentNodeResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentNodeResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEnvironmentNodeResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentNodeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionRelatedFoundationComponentVersionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ProductComponentRelationDetail] = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ProductComponentRelationDetail()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListProductVersionRelatedFoundationComponentVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProductVersionRelatedFoundationComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProductVersionRelatedFoundationComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncComponentRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        bucket_name: str = None,
    ):
        self.region = region
        self.bucket_name = bucket_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        return self


class SyncComponentResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SyncComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncComponentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SyncComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateComponentToProductRequest(TeaModel):
    def __init__(
        self,
        component_version_id: str = None,
    ):
        # the component Version ID
        self.component_version_id = component_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_version_id is not None:
            result['componentVersionID'] = self.component_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentVersionID') is not None:
            self.component_version_id = m.get('componentVersionID')
        return self


class UpdateComponentToProductResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateComponentToProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateComponentToProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateComponentToProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentNodeRequestDataDisk(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: int = None,
    ):
        self.name = name
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class CreateEnvironmentNodeRequestSystemDisk(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: int = None,
    ):
        self.name = name
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class CreateEnvironmentNodeRequestTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        self.effect = effect
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateEnvironmentNodeRequest(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        data_disk: List[CreateEnvironmentNodeRequestDataDisk] = None,
        host_name: str = None,
        identifier: str = None,
        labels: Dict[str, Any] = None,
        memory: int = None,
        os: str = None,
        private_ip: str = None,
        provider: str = None,
        root_password: str = None,
        system_disk: List[CreateEnvironmentNodeRequestSystemDisk] = None,
        taints: List[CreateEnvironmentNodeRequestTaints] = None,
    ):
        self.cpu = cpu
        self.data_disk = data_disk
        self.host_name = host_name
        self.identifier = identifier
        self.labels = labels
        self.memory = memory
        self.os = os
        self.private_ip = private_ip
        self.provider = provider
        self.root_password = root_password
        self.system_disk = system_disk
        self.taints = taints

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk:
            for k in self.system_disk:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        result['dataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['dataDisk'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.labels is not None:
            result['labels'] = self.labels
        if self.memory is not None:
            result['memory'] = self.memory
        if self.os is not None:
            result['os'] = self.os
        if self.private_ip is not None:
            result['privateIP'] = self.private_ip
        if self.provider is not None:
            result['provider'] = self.provider
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['systemDisk'] = []
        if self.system_disk is not None:
            for k in self.system_disk:
                result['systemDisk'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        self.data_disk = []
        if m.get('dataDisk') is not None:
            for k in m.get('dataDisk'):
                temp_model = CreateEnvironmentNodeRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('privateIP') is not None:
            self.private_ip = m.get('privateIP')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.system_disk = []
        if m.get('systemDisk') is not None:
            for k in m.get('systemDisk'):
                temp_model = CreateEnvironmentNodeRequestSystemDisk()
                self.system_disk.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = CreateEnvironmentNodeRequestTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class CreateEnvironmentNodeResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComponentResponseBodyDataAnnotations(TeaModel):
    def __init__(
        self,
        additional_prop_1: str = None,
        additional_prop_2: str = None,
        additional_prop_3: str = None,
    ):
        self.additional_prop_1 = additional_prop_1
        self.additional_prop_2 = additional_prop_2
        self.additional_prop_3 = additional_prop_3

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class GetComponentResponseBodyData(TeaModel):
    def __init__(
        self,
        annotations: GetComponentResponseBodyDataAnnotations = None,
        category: str = None,
        description: str = None,
        documents: str = None,
        name: str = None,
        provider: str = None,
        public: bool = None,
        singleton: bool = None,
        source: str = None,
        uid: str = None,
    ):
        self.annotations = annotations
        self.category = category
        self.description = description
        self.documents = documents
        self.name = name
        self.provider = provider
        self.public = public
        self.singleton = singleton
        self.source = source
        self.uid = uid

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = GetComponentResponseBodyDataAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetComponentResponseBody(TeaModel):
    def __init__(
        self,
        data: GetComponentResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetComponentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetComponentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationVersionRelatedComponentVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ComponentVersion] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ComponentVersion()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListFoundationVersionRelatedComponentVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListFoundationVersionRelatedComponentVersionsResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = ListFoundationVersionRelatedComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListFoundationVersionRelatedComponentVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFoundationVersionRelatedComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFoundationVersionRelatedComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSnapshotResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_cidr: str = None,
        name: str = None,
        product_name: str = None,
        product_version: str = None,
        product_version_desc: str = None,
        region: str = None,
        snapshot_region: str = None,
        snapshot_status: str = None,
        source_environment_uid: str = None,
        source_type: str = None,
        uid: str = None,
        vpcid: str = None,
    ):
        self.description = description
        self.instance_cidr = instance_cidr
        self.name = name
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_desc = product_version_desc
        self.region = region
        self.snapshot_region = snapshot_region
        self.snapshot_status = snapshot_status
        self.source_environment_uid = source_environment_uid
        self.source_type = source_type
        self.uid = uid
        self.vpcid = vpcid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.instance_cidr is not None:
            result['instanceCIDR'] = self.instance_cidr
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_desc is not None:
            result['productVersionDesc'] = self.product_version_desc
        if self.region is not None:
            result['region'] = self.region
        if self.snapshot_region is not None:
            result['snapshotRegion'] = self.snapshot_region
        if self.snapshot_status is not None:
            result['snapshotStatus'] = self.snapshot_status
        if self.source_environment_uid is not None:
            result['sourceEnvironmentUID'] = self.source_environment_uid
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vpcid is not None:
            result['vpcid'] = self.vpcid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceCIDR') is not None:
            self.instance_cidr = m.get('instanceCIDR')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionDesc') is not None:
            self.product_version_desc = m.get('productVersionDesc')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('snapshotRegion') is not None:
            self.snapshot_region = m.get('snapshotRegion')
        if m.get('snapshotStatus') is not None:
            self.snapshot_status = m.get('snapshotStatus')
        if m.get('sourceEnvironmentUID') is not None:
            self.source_environment_uid = m.get('sourceEnvironmentUID')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vpcid') is not None:
            self.vpcid = m.get('vpcid')
        return self


class GetSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSnapshotResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLicenseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLicenseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLatestProductVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateLatestProductVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateLatestProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateLatestProductVersionResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateLatestProductVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateLatestProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLatestProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLatestProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlicloudVPCResponseBodyDataVpcsVpcUserCidrs(TeaModel):
    def __init__(
        self,
        user_cidr: str = None,
    ):
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class ListAlicloudVPCResponseBodyDataVpcsVpcVSwitchIds(TeaModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ListAlicloudVPCResponseBodyDataVpcsVpc(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        creation_time: str = None,
        description: str = None,
        is_default: bool = None,
        region_id: str = None,
        status: str = None,
        user_cidrs: ListAlicloudVPCResponseBodyDataVpcsVpcUserCidrs = None,
        vrouter_id: str = None,
        v_switch_ids: ListAlicloudVPCResponseBodyDataVpcsVpcVSwitchIds = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.creation_time = creation_time
        self.description = description
        self.is_default = is_default
        self.region_id = region_id
        self.status = status
        self.user_cidrs = user_cidrs
        self.vrouter_id = vrouter_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        if self.user_cidrs:
            self.user_cidrs.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_cidrs is not None:
            result['UserCidrs'] = self.user_cidrs.to_map()
        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserCidrs') is not None:
            temp_model = ListAlicloudVPCResponseBodyDataVpcsVpcUserCidrs()
            self.user_cidrs = temp_model.from_map(m['UserCidrs'])
        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')
        if m.get('VSwitchIds') is not None:
            temp_model = ListAlicloudVPCResponseBodyDataVpcsVpcVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m['VSwitchIds'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class ListAlicloudVPCResponseBodyDataVpcs(TeaModel):
    def __init__(
        self,
        vpc: List[ListAlicloudVPCResponseBodyDataVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = ListAlicloudVPCResponseBodyDataVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class ListAlicloudVPCResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpcs: ListAlicloudVPCResponseBodyDataVpcs = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vpcs = vpcs

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Vpcs') is not None:
            temp_model = ListAlicloudVPCResponseBodyDataVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        return self


class ListAlicloudVPCResponseBody(TeaModel):
    def __init__(
        self,
        data: ListAlicloudVPCResponseBodyData = None,
        success: bool = None,
    ):
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListAlicloudVPCResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListAlicloudVPCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlicloudVPCResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlicloudVPCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateProductRequest(TeaModel):
    def __init__(
        self,
        annotations: str = None,
        component_version_uid: str = None,
        description: str = None,
        foundation_version_uid: str = None,
        product_name: str = None,
        prometheus_uid: str = None,
    ):
        self.annotations = annotations
        self.component_version_uid = component_version_uid
        self.description = description
        self.foundation_version_uid = foundation_version_uid
        self.product_name = product_name
        self.prometheus_uid = prometheus_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.prometheus_uid is not None:
            result['prometheusUID'] = self.prometheus_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('prometheusUID') is not None:
            self.prometheus_uid = m.get('prometheusUID')
        return self


class CreateProductResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateProductResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductEnvironmentsRequestPlatforms(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class GetProductEnvironmentsRequest(TeaModel):
    def __init__(
        self,
        product_uid: str = None,
        env_type: str = None,
        platforms: List[GetProductEnvironmentsRequestPlatforms] = None,
    ):
        self.product_uid = product_uid
        self.env_type = env_type
        self.platforms = platforms

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.env_type is not None:
            result['envType'] = self.env_type
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = GetProductEnvironmentsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        return self


class GetProductEnvironmentsShrinkRequest(TeaModel):
    def __init__(
        self,
        product_uid: str = None,
        env_type: str = None,
        platforms_shrink: str = None,
    ):
        self.product_uid = product_uid
        self.env_type = env_type
        self.platforms_shrink = platforms_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.env_type is not None:
            result['envType'] = self.env_type
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        return self


class GetProductEnvironmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        created_at: str = None,
        description: str = None,
        instance_list: str = None,
        name: str = None,
        product_name: str = None,
        product_version: str = None,
        uid: str = None,
        vendor_config: str = None,
        vendor_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.created_at = created_at
        self.description = description
        self.instance_list = instance_list
        self.name = name
        self.product_name = product_name
        self.product_version = product_version
        self.uid = uid
        self.vendor_config = vendor_config
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetProductEnvironmentsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetProductEnvironmentsResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteComponentResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteComponentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductComponentResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteProductComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProductComponentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProductComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentWithSnapshotRequest(TeaModel):
    def __init__(
        self,
        environment_desc: str = None,
        environment_name: str = None,
    ):
        self.environment_desc = environment_desc
        self.environment_name = environment_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_desc is not None:
            result['environmentDesc'] = self.environment_desc
        if self.environment_name is not None:
            result['environmentName'] = self.environment_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentDesc') is not None:
            self.environment_desc = m.get('environmentDesc')
        if m.get('environmentName') is not None:
            self.environment_name = m.get('environmentName')
        return self


class CreateEnvironmentWithSnapshotResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateEnvironmentWithSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateEnvironmentWithSnapshotResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateEnvironmentWithSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentWithSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEnvironmentWithSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentWithSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionRequest(TeaModel):
    def __init__(
        self,
        compatible_versions: str = None,
        description: str = None,
        version: str = None,
    ):
        self.compatible_versions = compatible_versions
        self.description = description
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_versions is not None:
            result['compatibleVersions'] = self.compatible_versions
        if self.description is not None:
            result['description'] = self.description
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compatibleVersions') is not None:
            self.compatible_versions = m.get('compatibleVersions')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpdateProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChildrenComponentVersionParametersListRequest(TeaModel):
    def __init__(
        self,
        relation_id: str = None,
    ):
        self.relation_id = relation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_id is not None:
            result['relation_id'] = self.relation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('relation_id') is not None:
            self.relation_id = m.get('relation_id')
        return self


class GetChildrenComponentVersionParametersListResponseBodyDataAnnotations(TeaModel):
    def __init__(
        self,
        additional_prop_1: str = None,
        additional_prop_2: str = None,
        additional_prop_3: str = None,
    ):
        self.additional_prop_1 = additional_prop_1
        self.additional_prop_2 = additional_prop_2
        self.additional_prop_3 = additional_prop_3

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class GetChildrenComponentVersionParametersListResponseBodyData(TeaModel):
    def __init__(
        self,
        annotations: GetChildrenComponentVersionParametersListResponseBodyDataAnnotations = None,
        category: str = None,
        class_: str = None,
        description: str = None,
        documents: List[str] = None,
        name: str = None,
        provider: str = None,
        uid: str = None,
    ):
        self.annotations = annotations
        self.category = category
        self.class_ = class_
        self.description = description
        self.documents = documents
        self.name = name
        self.provider = provider
        self.uid = uid

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.class_ is not None:
            result['class'] = self.class_
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = GetChildrenComponentVersionParametersListResponseBodyDataAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetChildrenComponentVersionParametersListResponseBody(TeaModel):
    def __init__(
        self,
        data: GetChildrenComponentVersionParametersListResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetChildrenComponentVersionParametersListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetChildrenComponentVersionParametersListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetChildrenComponentVersionParametersListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetChildrenComponentVersionParametersListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_name: str = None,
        product_version: str = None,
        product_version_desc: str = None,
        region: str = None,
        vpcid: str = None,
    ):
        self.description = description
        self.name = name
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_desc = product_version_desc
        self.region = region
        self.vpcid = vpcid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_desc is not None:
            result['productVersionDesc'] = self.product_version_desc
        if self.region is not None:
            result['region'] = self.region
        if self.vpcid is not None:
            result['vpcid'] = self.vpcid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionDesc') is not None:
            self.product_version_desc = m.get('productVersionDesc')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('vpcid') is not None:
            self.vpcid = m.get('vpcid')
        return self


class CreateSnapshotResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateSnapshotResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLatestVersionDifferencesRequest(TeaModel):
    def __init__(
        self,
        pre_version_id: str = None,
    ):
        # 上一个产品版本id
        self.pre_version_id = pre_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_version_id is not None:
            result['preVersionID'] = self.pre_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('preVersionID') is not None:
            self.pre_version_id = m.get('preVersionID')
        return self


class GetLatestVersionDifferencesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetLatestVersionDifferencesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLatestVersionDifferencesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLatestVersionDifferencesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentNodeRequest(TeaModel):
    def __init__(
        self,
        env_uid: str = None,
    ):
        self.env_uid = env_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        return self


class DeleteEnvironmentNodeResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteEnvironmentNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyComponentRequestPlatforms(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ApplyComponentRequest(TeaModel):
    def __init__(
        self,
        annotations: str = None,
        app_version: str = None,
        category: str = None,
        component_class: str = None,
        description: str = None,
        documents: str = None,
        images_mapping: str = None,
        name: str = None,
        namespace: str = None,
        orchestration_type: str = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        platforms: List[ApplyComponentRequestPlatforms] = None,
        priority: int = None,
        provider: str = None,
        public: bool = None,
        readme: str = None,
        resources: str = None,
        singleton: bool = None,
        version: str = None,
    ):
        self.annotations = annotations
        self.app_version = app_version
        self.category = category
        self.component_class = component_class
        self.description = description
        self.documents = documents
        self.images_mapping = images_mapping
        self.name = name
        self.namespace = namespace
        self.orchestration_type = orchestration_type
        self.orchestration_values = orchestration_values
        self.package_url = package_url
        self.parent_component = parent_component
        self.platforms = platforms
        self.priority = priority
        self.provider = provider
        self.public = public
        self.readme = readme
        self.resources = resources
        self.singleton = singleton
        self.version = version

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.component_class is not None:
            result['componentClass'] = self.component_class
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['priority'] = self.priority
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('componentClass') is not None:
            self.component_class = m.get('componentClass')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ApplyComponentRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ApplyComponentResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ApplyComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyComponentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApplyComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSnapshotInstancesRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_num: int = None,
        sort_key: str = None,
        sort_direct: str = None,
    ):
        self.page_size = page_size
        self.page_num = page_num
        self.sort_key = sort_key
        self.sort_direct = sort_direct

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        if self.sort_direct is not None:
            result['sortDirect'] = self.sort_direct
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        if m.get('sortDirect') is not None:
            self.sort_direct = m.get('sortDirect')
        return self


class GetSnapshotInstancesResponseBodyDataListAnnotations(TeaModel):
    def __init__(
        self,
        additional_prop_1: str = None,
        additional_prop_2: str = None,
        additional_prop_3: str = None,
    ):
        self.additional_prop_1 = additional_prop_1
        self.additional_prop_2 = additional_prop_2
        self.additional_prop_3 = additional_prop_3

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class GetSnapshotInstancesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        annotations: GetSnapshotInstancesResponseBodyDataListAnnotations = None,
        cpu: int = None,
        ecs_instance_id: str = None,
        host_name: str = None,
        identifier: str = None,
        image_id: str = None,
        instance_type: str = None,
        internet_bandwidth: int = None,
        join_snapshot: bool = None,
        memory: int = None,
        private_ip: str = None,
        public_ip: str = None,
        root_password: str = None,
        storage_total_size: int = None,
        uid: str = None,
    ):
        self.annotations = annotations
        self.cpu = cpu
        self.ecs_instance_id = ecs_instance_id
        self.host_name = host_name
        self.identifier = identifier
        self.image_id = image_id
        self.instance_type = instance_type
        self.internet_bandwidth = internet_bandwidth
        self.join_snapshot = join_snapshot
        self.memory = memory
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.root_password = root_password
        self.storage_total_size = storage_total_size
        self.uid = uid

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.ecs_instance_id is not None:
            result['ecsInstanceID'] = self.ecs_instance_id
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.image_id is not None:
            result['imageID'] = self.image_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_bandwidth is not None:
            result['internetBandwidth'] = self.internet_bandwidth
        if self.join_snapshot is not None:
            result['joinSnapshot'] = self.join_snapshot
        if self.memory is not None:
            result['memory'] = self.memory
        if self.private_ip is not None:
            result['privateIP'] = self.private_ip
        if self.public_ip is not None:
            result['publicIP'] = self.public_ip
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        if self.storage_total_size is not None:
            result['storageTotalSize'] = self.storage_total_size
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = GetSnapshotInstancesResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('ecsInstanceID') is not None:
            self.ecs_instance_id = m.get('ecsInstanceID')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('imageID') is not None:
            self.image_id = m.get('imageID')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetBandwidth') is not None:
            self.internet_bandwidth = m.get('internetBandwidth')
        if m.get('joinSnapshot') is not None:
            self.join_snapshot = m.get('joinSnapshot')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('privateIP') is not None:
            self.private_ip = m.get('privateIP')
        if m.get('publicIP') is not None:
            self.public_ip = m.get('publicIP')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        if m.get('storageTotalSize') is not None:
            self.storage_total_size = m.get('storageTotalSize')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetSnapshotInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[GetSnapshotInstancesResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetSnapshotInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetSnapshotInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSnapshotInstancesResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetSnapshotInstancesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetSnapshotInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSnapshotInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSnapshotInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        name: str = None,
        fuzzy: str = None,
        instance_status: str = None,
        vendor_type: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.name = name
        self.fuzzy = fuzzy
        self.instance_status = instance_status
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.name is not None:
            result['name'] = self.name
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsResponseBodyDataListPlatform(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListEnvironmentsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: int = None,
        location: str = None,
        name: str = None,
        platform: ListEnvironmentsResponseBodyDataListPlatform = None,
        product_name: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        uid: str = None,
        vendor_type: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.location = location
        self.name = name
        self.platform = platform
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.uid = uid
        self.vendor_type = vendor_type

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = ListEnvironmentsResponseBodyDataListPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListEnvironmentsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEnvironmentsResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSLRRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CheckSLRResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CheckSLRResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckSLRResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateProductResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyComponentsRequestChildrenListPlatforms(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ApplyComponentsRequestChildrenList(TeaModel):
    def __init__(
        self,
        annotations: str = None,
        app_version: str = None,
        category: str = None,
        component_class: str = None,
        description: str = None,
        documents: str = None,
        images_mapping: str = None,
        name: str = None,
        namespace: str = None,
        orchestration_type: str = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        platforms: List[ApplyComponentsRequestChildrenListPlatforms] = None,
        priority: int = None,
        provider: str = None,
        public: bool = None,
        readme: str = None,
        resources: str = None,
        singleton: bool = None,
        version: str = None,
    ):
        self.annotations = annotations
        self.app_version = app_version
        self.category = category
        self.component_class = component_class
        self.description = description
        self.documents = documents
        self.images_mapping = images_mapping
        self.name = name
        self.namespace = namespace
        self.orchestration_type = orchestration_type
        self.orchestration_values = orchestration_values
        self.package_url = package_url
        self.parent_component = parent_component
        self.platforms = platforms
        self.priority = priority
        self.provider = provider
        self.public = public
        self.readme = readme
        self.resources = resources
        self.singleton = singleton
        self.version = version

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.component_class is not None:
            result['componentClass'] = self.component_class
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['priority'] = self.priority
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('componentClass') is not None:
            self.component_class = m.get('componentClass')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ApplyComponentsRequestChildrenListPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ApplyComponentsRequest(TeaModel):
    def __init__(
        self,
        children_list: List[ApplyComponentsRequestChildrenList] = None,
        component: str = None,
    ):
        self.children_list = children_list
        self.component = component

    def validate(self):
        if self.children_list:
            for k in self.children_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['childrenList'] = []
        if self.children_list is not None:
            for k in self.children_list:
                result['childrenList'].append(k.to_map() if k else None)
        if self.component is not None:
            result['component'] = self.component
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children_list = []
        if m.get('childrenList') is not None:
            for k in m.get('childrenList'):
                temp_model = ApplyComponentsRequestChildrenList()
                self.children_list.append(temp_model.from_map(k))
        if m.get('component') is not None:
            self.component = m.get('component')
        return self


class ApplyComponentsResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ApplyComponentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyComponentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApplyComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePackageConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreatePackageConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: CreatePackageConfigResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreatePackageConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreatePackageConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePackageConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePackageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProductComponentRequest(TeaModel):
    def __init__(
        self,
        release_name: str = None,
    ):
        self.release_name = release_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        return self


class AddProductComponentResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddProductComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddProductComponentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddProductComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsWithSnapshotResponseBodyDataList(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: int = None,
        instance_status: str = None,
        name: str = None,
        product_name: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        uid: str = None,
        vendor_type: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.instance_status = instance_status
        self.name = name
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.uid = uid
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsWithSnapshotResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListEnvironmentsWithSnapshotResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentsWithSnapshotResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentsWithSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEnvironmentsWithSnapshotResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentsWithSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentsWithSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEnvironmentsWithSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentsWithSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentNodeResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        created_at: str = None,
        description: str = None,
        instance_list: str = None,
        name: str = None,
        product_name: str = None,
        product_version: str = None,
        uid: str = None,
        vendor_config: str = None,
        vendor_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.created_at = created_at
        self.description = description
        self.instance_list = instance_list
        self.name = name
        self.product_name = product_name
        self.product_version = product_version
        self.uid = uid
        self.vendor_config = vendor_config
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetEnvironmentNodeResponseBody(TeaModel):
    def __init__(
        self,
        data: GetEnvironmentNodeResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEnvironmentNodeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnvironmentNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        product_name: str = None,
        product_version: str = None,
        product_version_desc: str = None,
        update_key: str = None,
    ):
        self.description = description
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_desc = product_version_desc
        self.update_key = update_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_desc is not None:
            result['productVersionDesc'] = self.product_version_desc
        if self.update_key is not None:
            result['updateKey'] = self.update_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionDesc') is not None:
            self.product_version_desc = m.get('productVersionDesc')
        if m.get('updateKey') is not None:
            self.update_key = m.get('updateKey')
        return self


class UpdateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentAndGenerateVendorConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateEnvironmentAndGenerateVendorConfigRequestPlatform(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class CreateEnvironmentAndGenerateVendorConfigRequest(TeaModel):
    def __init__(
        self,
        env_uid: str = None,
        platform: CreateEnvironmentAndGenerateVendorConfigRequestPlatform = None,
        product_name: str = None,
        product_uid: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        vendor_type: str = None,
    ):
        self.env_uid = env_uid
        self.platform = platform
        self.product_name = product_name
        self.product_uid = product_uid
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.vendor_type = vendor_type

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('platform') is not None:
            temp_model = CreateEnvironmentAndGenerateVendorConfigRequestPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class CreateEnvironmentAndGenerateVendorConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        env_uid: str = None,
        vendor_config: str = None,
    ):
        self.env_uid = env_uid
        self.vendor_config = vendor_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class CreateEnvironmentAndGenerateVendorConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateEnvironmentAndGenerateVendorConfigResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateEnvironmentAndGenerateVendorConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentAndGenerateVendorConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEnvironmentAndGenerateVendorConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentAndGenerateVendorConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentSnapshotRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateEnvironmentSnapshotResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateEnvironmentSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateEnvironmentSnapshotResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateEnvironmentSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEnvironmentSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitSnapshotInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class InitSnapshotInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitSnapshotInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InitSnapshotInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionRelatedFoundationVersionRequest(TeaModel):
    def __init__(
        self,
        foundation_version_uid: str = None,
    ):
        self.foundation_version_uid = foundation_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        return self


class UpdateProductVersionRelatedFoundationVersionResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProductVersionRelatedFoundationVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProductVersionRelatedFoundationVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProductVersionRelatedFoundationVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentParamsRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        name: str = None,
        fuzzy: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.name = name
        self.fuzzy = fuzzy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.name is not None:
            result['name'] = self.name
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        return self


class ListEnvironmentParamsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        product_name: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        uid: str = None,
        vendor_type: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.uid = uid
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentParamsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListEnvironmentParamsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentParamsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentParamsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEnvironmentParamsResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentParamsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentParamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEnvironmentParamsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoundationVersionResponseBody(TeaModel):
    def __init__(
        self,
        data: List[FoundationVersion] = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = FoundationVersion()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetFoundationVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFoundationVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFoundationVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        location: str = None,
        vendor_config: str = None,
    ):
        self.description = description
        self.location = location
        self.vendor_config = vendor_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.location is not None:
            result['location'] = self.location
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class UpdateEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentPackageResponseBodyData(TeaModel):
    def __init__(
        self,
        package_url: str = None,
    ):
        self.package_url = package_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        return self


class GetEnvironmentPackageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetEnvironmentPackageResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEnvironmentPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnvironmentPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEnvironmentPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductComponentDetailResponseBodyDataChildrenComponentVersionList(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        category: str = None,
        class_: str = None,
        component_name: str = None,
        component_uid: str = None,
        description: str = None,
        documents: List[str] = None,
        enable: bool = None,
        images_mapping: str = None,
        namespace: str = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        priority: int = None,
        product_component_version_uid: str = None,
        provider: str = None,
        readme: str = None,
        resources: str = None,
        singleton: bool = None,
        uid: str = None,
        version: str = None,
    ):
        self.app_version = app_version
        self.category = category
        self.class_ = class_
        self.component_name = component_name
        self.component_uid = component_uid
        self.description = description
        self.documents = documents
        self.enable = enable
        self.images_mapping = images_mapping
        self.namespace = namespace
        self.orchestration_values = orchestration_values
        self.package_url = package_url
        self.parent_component = parent_component
        self.priority = priority
        self.product_component_version_uid = product_component_version_uid
        self.provider = provider
        self.readme = readme
        self.resources = resources
        self.singleton = singleton
        self.uid = uid
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.class_ is not None:
            result['class'] = self.class_
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.enable is not None:
            result['enable'] = self.enable
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.priority is not None:
            result['priority'] = self.priority
        if self.product_component_version_uid is not None:
            result['productComponentVersionUID'] = self.product_component_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('productComponentVersionUID') is not None:
            self.product_component_version_uid = m.get('productComponentVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductComponentDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        category: str = None,
        children_component_version_list: List[GetProductComponentDetailResponseBodyDataChildrenComponentVersionList] = None,
        class_: str = None,
        component_name: str = None,
        component_uid: str = None,
        description: str = None,
        documents: List[str] = None,
        enable: bool = None,
        has_dependency: bool = None,
        images_mapping: str = None,
        namespace: str = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        priority: int = None,
        product_component_version_uid: str = None,
        provider: str = None,
        readme: str = None,
        resources: str = None,
        singleton: bool = None,
        uid: str = None,
        version: str = None,
    ):
        self.app_version = app_version
        self.category = category
        self.children_component_version_list = children_component_version_list
        self.class_ = class_
        self.component_name = component_name
        self.component_uid = component_uid
        self.description = description
        self.documents = documents
        self.enable = enable
        self.has_dependency = has_dependency
        self.images_mapping = images_mapping
        self.namespace = namespace
        self.orchestration_values = orchestration_values
        self.package_url = package_url
        self.parent_component = parent_component
        self.priority = priority
        self.product_component_version_uid = product_component_version_uid
        self.provider = provider
        self.readme = readme
        self.resources = resources
        self.singleton = singleton
        self.uid = uid
        self.version = version

    def validate(self):
        if self.children_component_version_list:
            for k in self.children_component_version_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        result['childrenComponentVersionList'] = []
        if self.children_component_version_list is not None:
            for k in self.children_component_version_list:
                result['childrenComponentVersionList'].append(k.to_map() if k else None)
        if self.class_ is not None:
            result['class'] = self.class_
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.enable is not None:
            result['enable'] = self.enable
        if self.has_dependency is not None:
            result['hasDependency'] = self.has_dependency
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.priority is not None:
            result['priority'] = self.priority
        if self.product_component_version_uid is not None:
            result['productComponentVersionUID'] = self.product_component_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        self.children_component_version_list = []
        if m.get('childrenComponentVersionList') is not None:
            for k in m.get('childrenComponentVersionList'):
                temp_model = GetProductComponentDetailResponseBodyDataChildrenComponentVersionList()
                self.children_component_version_list.append(temp_model.from_map(k))
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('hasDependency') is not None:
            self.has_dependency = m.get('hasDependency')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('productComponentVersionUID') is not None:
            self.product_component_version_uid = m.get('productComponentVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductComponentDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: GetProductComponentDetailResponseBodyData = None,
        err_code: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductComponentDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductComponentDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductComponentDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductComponentDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportEnvironmentNodesRequest(TeaModel):
    def __init__(
        self,
        node_list_yaml: str = None,
    ):
        self.node_list_yaml = node_list_yaml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_list_yaml is not None:
            result['nodeListYaml'] = self.node_list_yaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeListYaml') is not None:
            self.node_list_yaml = m.get('nodeListYaml')
        return self


class ImportEnvironmentNodesResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ImportEnvironmentNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportEnvironmentNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        category: str = None,
        page_num: int = None,
        page_size: int = None,
        fuzzy: str = None,
        public: bool = None,
    ):
        self.name = name
        self.category = category
        self.page_num = page_num
        self.page_size = page_size
        self.fuzzy = fuzzy
        self.public = public

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.category is not None:
            result['category'] = self.category
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('public') is not None:
            self.public = m.get('public')
        return self


class ListComponentsResponseBodyDataListAnnotations(TeaModel):
    def __init__(
        self,
        annotations: str = None,
    ):
        self.annotations = annotations

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        return self


class ListComponentsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        annotations: ListComponentsResponseBodyDataListAnnotations = None,
        category: str = None,
        description: str = None,
        documents: str = None,
        name: str = None,
        provider: str = None,
        public: bool = None,
        singleton: bool = None,
        source: str = None,
        uid: str = None,
    ):
        self.annotations = annotations
        self.category = category
        self.description = description
        self.documents = documents
        self.name = name
        self.provider = provider
        self.public = public
        self.singleton = singleton
        self.source = source
        self.uid = uid

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = ListComponentsResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListComponentsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListComponentsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListComponentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListComponentsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListComponentsResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListComponentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListComponentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListComponentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEnvironmentProductVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddEnvironmentProductVersionRequest(TeaModel):
    def __init__(
        self,
        product_name: str = None,
        product_uid: str = None,
        product_version: str = None,
        product_version_uid: str = None,
    ):
        self.product_name = product_name
        self.product_uid = product_uid
        self.product_version = product_version
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class AddEnvironmentProductVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class AddEnvironmentProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        data: AddEnvironmentProductVersionResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = AddEnvironmentProductVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddEnvironmentProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddEnvironmentProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddEnvironmentProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionsRequestPlatforms(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListProductVersionsRequest(TeaModel):
    def __init__(
        self,
        released: bool = None,
        platforms: List[ListProductVersionsRequestPlatforms] = None,
    ):
        self.released = released
        self.platforms = platforms

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.released is not None:
            result['released'] = self.released
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('released') is not None:
            self.released = m.get('released')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListProductVersionsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        return self


class ListProductVersionsShrinkRequest(TeaModel):
    def __init__(
        self,
        released: bool = None,
        platforms_shrink: str = None,
    ):
        self.released = released
        self.platforms_shrink = platforms_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.released is not None:
            result['released'] = self.released
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('released') is not None:
            self.released = m.get('released')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        return self


class ListProductVersionsResponseBodyDataListAnnotations(TeaModel):
    def __init__(
        self,
        additional_prop_1: str = None,
        additional_prop_2: str = None,
        additional_prop_3: str = None,
    ):
        self.additional_prop_1 = additional_prop_1
        self.additional_prop_2 = additional_prop_2
        self.additional_prop_3 = additional_prop_3

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class ListProductVersionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        annotations: ListProductVersionsResponseBodyDataListAnnotations = None,
        description: str = None,
        package_url: str = None,
        product_name: str = None,
        product_uid: str = None,
        provider: str = None,
        uid: str = None,
        version: str = None,
    ):
        self.annotations = annotations
        self.description = description
        self.package_url = package_url
        self.product_name = product_name
        self.product_uid = product_uid
        self.provider = provider
        self.uid = uid
        self.version = version

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = ListProductVersionsResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListProductVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListProductVersionsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductVersionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductVersionsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListProductVersionsResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProductVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListProductVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProductVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProductVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChildrenComponentVersionListResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        created_at: str = None,
        description: str = None,
        instance_list: str = None,
        name: str = None,
        product_name: str = None,
        product_version: str = None,
        uid: str = None,
        vendor_config: str = None,
        vendor_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.created_at = created_at
        self.description = description
        self.instance_list = instance_list
        self.name = name
        self.product_name = product_name
        self.product_version = product_version
        self.uid = uid
        self.vendor_config = vendor_config
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetChildrenComponentVersionListResponseBody(TeaModel):
    def __init__(
        self,
        data: GetChildrenComponentVersionListResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetChildrenComponentVersionListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetChildrenComponentVersionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetChildrenComponentVersionListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetChildrenComponentVersionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSLRHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSLRResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSLRResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSLRResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionRelatedComponentVersionDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ProductComponentRelationDetail] = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ProductComponentRelationDetail()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductVersionRelatedComponentVersionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductVersionRelatedComponentVersionDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductVersionRelatedComponentVersionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEnvironmentPackageHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddEnvironmentPackageRequest(TeaModel):
    def __init__(
        self,
        package_type: str = None,
    ):
        self.package_type = package_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_type is not None:
            result['packageType'] = self.package_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        return self


class AddEnvironmentPackageResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddEnvironmentPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddEnvironmentPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddEnvironmentPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentProductVersionRequest(TeaModel):
    def __init__(
        self,
        compatible_versions: str = None,
        old_product_version: str = None,
        old_product_version_uid: str = None,
        product_name: str = None,
        product_uid: str = None,
        product_version: str = None,
        product_version_uid: str = None,
    ):
        self.compatible_versions = compatible_versions
        self.old_product_version = old_product_version
        self.old_product_version_uid = old_product_version_uid
        self.product_name = product_name
        self.product_uid = product_uid
        self.product_version = product_version
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_versions is not None:
            result['compatibleVersions'] = self.compatible_versions
        if self.old_product_version is not None:
            result['oldProductVersion'] = self.old_product_version
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compatibleVersions') is not None:
            self.compatible_versions = m.get('compatibleVersions')
        if m.get('oldProductVersion') is not None:
            self.old_product_version = m.get('oldProductVersion')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class UpdateEnvironmentProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateEnvironmentProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEnvironmentProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionPlatformsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class GetProductVersionPlatformsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[GetProductVersionPlatformsResponseBodyDataList] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetProductVersionPlatformsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class GetProductVersionPlatformsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetProductVersionPlatformsResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductVersionPlatformsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductVersionPlatformsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductVersionPlatformsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductVersionPlatformsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveEnvironmentParamRequest(TeaModel):
    def __init__(
        self,
        component_uid: str = None,
        component_version_uid: str = None,
        name: str = None,
        param_uid: str = None,
        provider: str = None,
        release_name: str = None,
        scope: List[str] = None,
        value: str = None,
    ):
        self.component_uid = component_uid
        self.component_version_uid = component_version_uid
        self.name = name
        self.param_uid = param_uid
        self.provider = provider
        self.release_name = release_name
        self.scope = scope
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.name is not None:
            result['name'] = self.name
        if self.param_uid is not None:
            result['paramUID'] = self.param_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('paramUID') is not None:
            self.param_uid = m.get('paramUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SaveEnvironmentParamResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SaveEnvironmentParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveEnvironmentParamResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveEnvironmentParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotInstanceJoinOptionRequest(TeaModel):
    def __init__(
        self,
        join_snapshot: bool = None,
        root_password: str = None,
    ):
        self.join_snapshot = join_snapshot
        self.root_password = root_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_snapshot is not None:
            result['joinSnapshot'] = self.join_snapshot
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('joinSnapshot') is not None:
            self.join_snapshot = m.get('joinSnapshot')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        return self


class UpdateSnapshotInstanceJoinOptionResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateSnapshotInstanceJoinOptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSnapshotInstanceJoinOptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSnapshotInstanceJoinOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionResourceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductVersionResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductVersionResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductVersionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLicenseRequest(TeaModel):
    def __init__(
        self,
        effective_year: int = None,
    ):
        # expire time
        self.effective_year = effective_year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_year is not None:
            result['effectiveYear'] = self.effective_year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effectiveYear') is not None:
            self.effective_year = m.get('effectiveYear')
        return self


class CreateLicenseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLicenseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShareSnapshotRequest(TeaModel):
    def __init__(
        self,
        target_provider: str = None,
    ):
        self.target_provider = target_provider

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_provider is not None:
            result['targetProvider'] = self.target_provider
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetProvider') is not None:
            self.target_provider = m.get('targetProvider')
        return self


class ShareSnapshotResponseBodyData(TeaModel):
    def __init__(
        self,
        new_snapshot_uid: str = None,
    ):
        self.new_snapshot_uid = new_snapshot_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_snapshot_uid is not None:
            result['newSnapshotUID'] = self.new_snapshot_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newSnapshotUID') is not None:
            self.new_snapshot_uid = m.get('newSnapshotUID')
        return self


class ShareSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        data: ShareSnapshotResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ShareSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ShareSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ShareSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ShareSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentParamResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteEnvironmentParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEnvironmentParamResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        provider: str = None,
        uid: str = None,
    ):
        self.description = description
        self.name = name
        self.provider = provider
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetProductResponseBody(TeaModel):
    def __init__(
        self,
        data: GetProductResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteComponentVersionResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        success: bool = None,
    ):
        self.err_message = err_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteComponentVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployEnvironmentProductResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployEnvironmentProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployEnvironmentProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeployEnvironmentProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitEnvironmentResourceRequest(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyID'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyID') is not None:
            self.access_key_id = m.get('accessKeyID')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        return self


class InitEnvironmentResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class InitEnvironmentResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: InitEnvironmentResourceResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = InitEnvironmentResourceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class InitEnvironmentResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitEnvironmentResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InitEnvironmentResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationVersionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[FoundationVersion] = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = FoundationVersion()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListFoundationVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFoundationVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFoundationVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentDeployRecordRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnvironmentDeployRecordResponseBodyDataList(TeaModel):
    def __init__(
        self,
        env_uid: str = None,
        provider: str = None,
        status: str = None,
        uid: str = None,
    ):
        self.env_uid = env_uid
        self.provider = provider
        self.status = status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnvironmentDeployRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListEnvironmentDeployRecordResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentDeployRecordResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentDeployRecordResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEnvironmentDeployRecordResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentDeployRecordResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentDeployRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEnvironmentDeployRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentDeployRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


