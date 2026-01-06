# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class AddFolderResponseBody(DaraModel):
    def __init__(
        self,
        dentry: main_models.AddFolderResponseBodyDentry = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.dentry = dentry
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.dentry:
            self.dentry.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry is not None:
            result['dentry'] = self.dentry.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dentry') is not None:
            temp_model = main_models.AddFolderResponseBodyDentry()
            self.dentry = temp_model.from_map(m.get('dentry'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class AddFolderResponseBodyDentry(DaraModel):
    def __init__(
        self,
        app_properties: Dict[str, List[main_models.DentryAppPropertiesValue]] = None,
        create_time: str = None,
        creator_id: str = None,
        extension: str = None,
        id: str = None,
        modified_time: str = None,
        modifier_id: str = None,
        name: str = None,
        parent_id: str = None,
        partition_type: str = None,
        path: str = None,
        properties: main_models.AddFolderResponseBodyDentryProperties = None,
        size: int = None,
        space_id: str = None,
        status: str = None,
        storage_driver: str = None,
        type: str = None,
        uuid: str = None,
        version: int = None,
    ):
        self.app_properties = app_properties
        self.create_time = create_time
        self.creator_id = creator_id
        self.extension = extension
        self.id = id
        self.modified_time = modified_time
        self.modifier_id = modifier_id
        self.name = name
        self.parent_id = parent_id
        self.partition_type = partition_type
        self.path = path
        self.properties = properties
        self.size = size
        self.space_id = space_id
        self.status = status
        self.storage_driver = storage_driver
        self.type = type
        self.uuid = uuid
        self.version = version

    def validate(self):
        if self.app_properties:
            for v1 in self.app_properties.values():
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.properties:
            self.properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppProperties'] = {}
        if self.app_properties is not None:
            for k1, v1 in self.app_properties.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['AppProperties'][k1] = l1

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.id is not None:
            result['Id'] = self.id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type

        if self.path is not None:
            result['Path'] = self.path

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.size is not None:
            result['Size'] = self.size

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_driver is not None:
            result['StorageDriver'] = self.storage_driver

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_properties = {}
        if m.get('AppProperties') is not None:
            for k1, v1 in m.get('AppProperties').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.DentryAppPropertiesValue()
                    l1.append(temp_model.from_map(k2))
                self.app_properties[k1] = l1

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Properties') is not None:
            temp_model = main_models.AddFolderResponseBodyDentryProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageDriver') is not None:
            self.storage_driver = m.get('StorageDriver')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class AddFolderResponseBodyDentryProperties(DaraModel):
    def __init__(
        self,
        read_only: bool = None,
    ):
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        return self

