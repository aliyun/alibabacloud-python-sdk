# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeRdsAnalysisResourceQuotasResponseBody(DaraModel):
    def __init__(
        self,
        dbnode_category_list: main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeCategoryList = None,
        dbnode_class_list: main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeClassList = None,
        dbnode_storage_list: main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeStorageList = None,
        engine_version_list: main_models.DescribeRdsAnalysisResourceQuotasResponseBodyEngineVersionList = None,
        mode_list: main_models.DescribeRdsAnalysisResourceQuotasResponseBodyModeList = None,
        request_id: str = None,
        storage_type_list: main_models.DescribeRdsAnalysisResourceQuotasResponseBodyStorageTypeList = None,
    ):
        self.dbnode_category_list = dbnode_category_list
        self.dbnode_class_list = dbnode_class_list
        self.dbnode_storage_list = dbnode_storage_list
        self.engine_version_list = engine_version_list
        self.mode_list = mode_list
        # The request ID.
        self.request_id = request_id
        self.storage_type_list = storage_type_list

    def validate(self):
        if self.dbnode_category_list:
            self.dbnode_category_list.validate()
        if self.dbnode_class_list:
            self.dbnode_class_list.validate()
        if self.dbnode_storage_list:
            self.dbnode_storage_list.validate()
        if self.engine_version_list:
            self.engine_version_list.validate()
        if self.mode_list:
            self.mode_list.validate()
        if self.storage_type_list:
            self.storage_type_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_category_list is not None:
            result['DBNodeCategoryList'] = self.dbnode_category_list.to_map()

        if self.dbnode_class_list is not None:
            result['DBNodeClassList'] = self.dbnode_class_list.to_map()

        if self.dbnode_storage_list is not None:
            result['DBNodeStorageList'] = self.dbnode_storage_list.to_map()

        if self.engine_version_list is not None:
            result['EngineVersionList'] = self.engine_version_list.to_map()

        if self.mode_list is not None:
            result['ModeList'] = self.mode_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.storage_type_list is not None:
            result['StorageTypeList'] = self.storage_type_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeCategoryList') is not None:
            temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeCategoryList()
            self.dbnode_category_list = temp_model.from_map(m.get('DBNodeCategoryList'))

        if m.get('DBNodeClassList') is not None:
            temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeClassList()
            self.dbnode_class_list = temp_model.from_map(m.get('DBNodeClassList'))

        if m.get('DBNodeStorageList') is not None:
            temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeStorageList()
            self.dbnode_storage_list = temp_model.from_map(m.get('DBNodeStorageList'))

        if m.get('EngineVersionList') is not None:
            temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyEngineVersionList()
            self.engine_version_list = temp_model.from_map(m.get('EngineVersionList'))

        if m.get('ModeList') is not None:
            temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyModeList()
            self.mode_list = temp_model.from_map(m.get('ModeList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StorageTypeList') is not None:
            temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyStorageTypeList()
            self.storage_type_list = temp_model.from_map(m.get('StorageTypeList'))

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyStorageTypeList(DaraModel):
    def __init__(
        self,
        storage_type: List[main_models.DescribeRdsAnalysisResourceQuotasResponseBodyStorageTypeListStorageType] = None,
    ):
        self.storage_type = storage_type

    def validate(self):
        if self.storage_type:
            for v1 in self.storage_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StorageType'] = []
        if self.storage_type is not None:
            for k1 in self.storage_type:
                result['StorageType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_type = []
        if m.get('StorageType') is not None:
            for k1 in m.get('StorageType'):
                temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyStorageTypeListStorageType()
                self.storage_type.append(temp_model.from_map(k1))

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyStorageTypeListStorageType(DaraModel):
    def __init__(
        self,
        text: str = None,
        value: str = None,
    ):
        self.text = text
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyModeList(DaraModel):
    def __init__(
        self,
        mode: List[main_models.DescribeRdsAnalysisResourceQuotasResponseBodyModeListMode] = None,
    ):
        self.mode = mode

    def validate(self):
        if self.mode:
            for v1 in self.mode:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Mode'] = []
        if self.mode is not None:
            for k1 in self.mode:
                result['Mode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mode = []
        if m.get('Mode') is not None:
            for k1 in m.get('Mode'):
                temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyModeListMode()
                self.mode.append(temp_model.from_map(k1))

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyModeListMode(DaraModel):
    def __init__(
        self,
        text: str = None,
        value: str = None,
    ):
        self.text = text
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyEngineVersionList(DaraModel):
    def __init__(
        self,
        engine_version: List[main_models.DescribeRdsAnalysisResourceQuotasResponseBodyEngineVersionListEngineVersion] = None,
    ):
        self.engine_version = engine_version

    def validate(self):
        if self.engine_version:
            for v1 in self.engine_version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EngineVersion'] = []
        if self.engine_version is not None:
            for k1 in self.engine_version:
                result['EngineVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.engine_version = []
        if m.get('EngineVersion') is not None:
            for k1 in m.get('EngineVersion'):
                temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyEngineVersionListEngineVersion()
                self.engine_version.append(temp_model.from_map(k1))

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyEngineVersionListEngineVersion(DaraModel):
    def __init__(
        self,
        text: str = None,
        value: str = None,
    ):
        self.text = text
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeStorageList(DaraModel):
    def __init__(
        self,
        dbnode_storage: List[main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeStorageListDBNodeStorage] = None,
    ):
        self.dbnode_storage = dbnode_storage

    def validate(self):
        if self.dbnode_storage:
            for v1 in self.dbnode_storage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBNodeStorage'] = []
        if self.dbnode_storage is not None:
            for k1 in self.dbnode_storage:
                result['DBNodeStorage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbnode_storage = []
        if m.get('DBNodeStorage') is not None:
            for k1 in m.get('DBNodeStorage'):
                temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeStorageListDBNodeStorage()
                self.dbnode_storage.append(temp_model.from_map(k1))

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeStorageListDBNodeStorage(DaraModel):
    def __init__(
        self,
        text: str = None,
        value: str = None,
    ):
        self.text = text
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeClassList(DaraModel):
    def __init__(
        self,
        dbnode_class: List[main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeClassListDBNodeClass] = None,
    ):
        self.dbnode_class = dbnode_class

    def validate(self):
        if self.dbnode_class:
            for v1 in self.dbnode_class:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBNodeClass'] = []
        if self.dbnode_class is not None:
            for k1 in self.dbnode_class:
                result['DBNodeClass'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbnode_class = []
        if m.get('DBNodeClass') is not None:
            for k1 in m.get('DBNodeClass'):
                temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeClassListDBNodeClass()
                self.dbnode_class.append(temp_model.from_map(k1))

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeClassListDBNodeClass(DaraModel):
    def __init__(
        self,
        text: str = None,
        value: str = None,
    ):
        self.text = text
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeCategoryList(DaraModel):
    def __init__(
        self,
        dbnode_category: List[main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeCategoryListDBNodeCategory] = None,
    ):
        self.dbnode_category = dbnode_category

    def validate(self):
        if self.dbnode_category:
            for v1 in self.dbnode_category:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBNodeCategory'] = []
        if self.dbnode_category is not None:
            for k1 in self.dbnode_category:
                result['DBNodeCategory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbnode_category = []
        if m.get('DBNodeCategory') is not None:
            for k1 in m.get('DBNodeCategory'):
                temp_model = main_models.DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeCategoryListDBNodeCategory()
                self.dbnode_category.append(temp_model.from_map(k1))

        return self

class DescribeRdsAnalysisResourceQuotasResponseBodyDBNodeCategoryListDBNodeCategory(DaraModel):
    def __init__(
        self,
        text: str = None,
        value: str = None,
    ):
        self.text = text
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

