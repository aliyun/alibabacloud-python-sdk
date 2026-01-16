# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class GetRegionalInstanceConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetRegionalInstanceConfigResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetRegionalInstanceConfigResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetRegionalInstanceConfigResponseBodyResult(DaraModel):
    def __init__(
        self,
        client_node_amount_range: main_models.GetRegionalInstanceConfigResponseBodyResultClientNodeAmountRange = None,
        client_node_disk_list: List[main_models.GetRegionalInstanceConfigResponseBodyResultClientNodeDiskList] = None,
        client_specs: List[str] = None,
        data_node_amount_range: main_models.GetRegionalInstanceConfigResponseBodyResultDataNodeAmountRange = None,
        data_node_disk_list: List[main_models.GetRegionalInstanceConfigResponseBodyResultDataNodeDiskList] = None,
        data_node_specs: List[str] = None,
        kibana_specs: List[str] = None,
        master_amount_range: List[str] = None,
        master_disk_list: List[main_models.GetRegionalInstanceConfigResponseBodyResultMasterDiskList] = None,
        master_specs: List[str] = None,
        spec_info_map: Dict[str, main_models.ResultSpecInfoMapValue] = None,
        versions: List[str] = None,
        warm_node_amount_range: main_models.GetRegionalInstanceConfigResponseBodyResultWarmNodeAmountRange = None,
        warm_node_disk_list: List[main_models.GetRegionalInstanceConfigResponseBodyResultWarmNodeDiskList] = None,
        warm_node_specs: List[str] = None,
    ):
        self.client_node_amount_range = client_node_amount_range
        self.client_node_disk_list = client_node_disk_list
        self.client_specs = client_specs
        self.data_node_amount_range = data_node_amount_range
        self.data_node_disk_list = data_node_disk_list
        self.data_node_specs = data_node_specs
        self.kibana_specs = kibana_specs
        self.master_amount_range = master_amount_range
        self.master_disk_list = master_disk_list
        self.master_specs = master_specs
        self.spec_info_map = spec_info_map
        self.versions = versions
        self.warm_node_amount_range = warm_node_amount_range
        self.warm_node_disk_list = warm_node_disk_list
        self.warm_node_specs = warm_node_specs

    def validate(self):
        if self.client_node_amount_range:
            self.client_node_amount_range.validate()
        if self.client_node_disk_list:
            for v1 in self.client_node_disk_list:
                 if v1:
                    v1.validate()
        if self.data_node_amount_range:
            self.data_node_amount_range.validate()
        if self.data_node_disk_list:
            for v1 in self.data_node_disk_list:
                 if v1:
                    v1.validate()
        if self.master_disk_list:
            for v1 in self.master_disk_list:
                 if v1:
                    v1.validate()
        if self.spec_info_map:
            for v1 in self.spec_info_map.values():
                 if v1:
                    v1.validate()
        if self.warm_node_amount_range:
            self.warm_node_amount_range.validate()
        if self.warm_node_disk_list:
            for v1 in self.warm_node_disk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_node_amount_range is not None:
            result['clientNodeAmountRange'] = self.client_node_amount_range.to_map()

        result['clientNodeDiskList'] = []
        if self.client_node_disk_list is not None:
            for k1 in self.client_node_disk_list:
                result['clientNodeDiskList'].append(k1.to_map() if k1 else None)

        if self.client_specs is not None:
            result['clientSpecs'] = self.client_specs

        if self.data_node_amount_range is not None:
            result['dataNodeAmountRange'] = self.data_node_amount_range.to_map()

        result['dataNodeDiskList'] = []
        if self.data_node_disk_list is not None:
            for k1 in self.data_node_disk_list:
                result['dataNodeDiskList'].append(k1.to_map() if k1 else None)

        if self.data_node_specs is not None:
            result['dataNodeSpecs'] = self.data_node_specs

        if self.kibana_specs is not None:
            result['kibanaSpecs'] = self.kibana_specs

        if self.master_amount_range is not None:
            result['masterAmountRange'] = self.master_amount_range

        result['masterDiskList'] = []
        if self.master_disk_list is not None:
            for k1 in self.master_disk_list:
                result['masterDiskList'].append(k1.to_map() if k1 else None)

        if self.master_specs is not None:
            result['masterSpecs'] = self.master_specs

        result['specInfoMap'] = {}
        if self.spec_info_map is not None:
            for k1, v1 in self.spec_info_map.items():
                result['specInfoMap'][k1] = v1.to_map() if v1 else None

        if self.versions is not None:
            result['versions'] = self.versions

        if self.warm_node_amount_range is not None:
            result['warmNodeAmountRange'] = self.warm_node_amount_range.to_map()

        result['warmNodeDiskList'] = []
        if self.warm_node_disk_list is not None:
            for k1 in self.warm_node_disk_list:
                result['warmNodeDiskList'].append(k1.to_map() if k1 else None)

        if self.warm_node_specs is not None:
            result['warmNodeSpecs'] = self.warm_node_specs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientNodeAmountRange') is not None:
            temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultClientNodeAmountRange()
            self.client_node_amount_range = temp_model.from_map(m.get('clientNodeAmountRange'))

        self.client_node_disk_list = []
        if m.get('clientNodeDiskList') is not None:
            for k1 in m.get('clientNodeDiskList'):
                temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultClientNodeDiskList()
                self.client_node_disk_list.append(temp_model.from_map(k1))

        if m.get('clientSpecs') is not None:
            self.client_specs = m.get('clientSpecs')

        if m.get('dataNodeAmountRange') is not None:
            temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultDataNodeAmountRange()
            self.data_node_amount_range = temp_model.from_map(m.get('dataNodeAmountRange'))

        self.data_node_disk_list = []
        if m.get('dataNodeDiskList') is not None:
            for k1 in m.get('dataNodeDiskList'):
                temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultDataNodeDiskList()
                self.data_node_disk_list.append(temp_model.from_map(k1))

        if m.get('dataNodeSpecs') is not None:
            self.data_node_specs = m.get('dataNodeSpecs')

        if m.get('kibanaSpecs') is not None:
            self.kibana_specs = m.get('kibanaSpecs')

        if m.get('masterAmountRange') is not None:
            self.master_amount_range = m.get('masterAmountRange')

        self.master_disk_list = []
        if m.get('masterDiskList') is not None:
            for k1 in m.get('masterDiskList'):
                temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultMasterDiskList()
                self.master_disk_list.append(temp_model.from_map(k1))

        if m.get('masterSpecs') is not None:
            self.master_specs = m.get('masterSpecs')

        self.spec_info_map = {}
        if m.get('specInfoMap') is not None:
            for k1, v1 in m.get('specInfoMap').items():
                temp_model = main_models.ResultSpecInfoMapValue()
                self.spec_info_map[k1] = temp_model.from_map(v1)

        if m.get('versions') is not None:
            self.versions = m.get('versions')

        if m.get('warmNodeAmountRange') is not None:
            temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultWarmNodeAmountRange()
            self.warm_node_amount_range = temp_model.from_map(m.get('warmNodeAmountRange'))

        self.warm_node_disk_list = []
        if m.get('warmNodeDiskList') is not None:
            for k1 in m.get('warmNodeDiskList'):
                temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultWarmNodeDiskList()
                self.warm_node_disk_list.append(temp_model.from_map(k1))

        if m.get('warmNodeSpecs') is not None:
            self.warm_node_specs = m.get('warmNodeSpecs')

        return self

class GetRegionalInstanceConfigResponseBodyResultWarmNodeDiskList(DaraModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
        sub_classification_confines: List[main_models.GetRegionalInstanceConfigResponseBodyResultWarmNodeDiskListSubClassificationConfines] = None,
        value_limit_set: List[int] = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit
        self.sub_classification_confines = sub_classification_confines
        self.value_limit_set = value_limit_set

    def validate(self):
        if self.sub_classification_confines:
            for v1 in self.sub_classification_confines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit

        result['subClassificationConfines'] = []
        if self.sub_classification_confines is not None:
            for k1 in self.sub_classification_confines:
                result['subClassificationConfines'].append(k1.to_map() if k1 else None)

        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')

        self.sub_classification_confines = []
        if m.get('subClassificationConfines') is not None:
            for k1 in m.get('subClassificationConfines'):
                temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultWarmNodeDiskListSubClassificationConfines()
                self.sub_classification_confines.append(temp_model.from_map(k1))

        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')

        return self

class GetRegionalInstanceConfigResponseBodyResultWarmNodeDiskListSubClassificationConfines(DaraModel):
    def __init__(
        self,
        max_size: int = None,
        min_size: int = None,
        performance_level: str = None,
    ):
        self.max_size = max_size
        self.min_size = min_size
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')

        return self

class GetRegionalInstanceConfigResponseBodyResultWarmNodeAmountRange(DaraModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount

        if self.min_amount is not None:
            result['minAmount'] = self.min_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')

        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')

        return self

class GetRegionalInstanceConfigResponseBodyResultMasterDiskList(DaraModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
        sub_classification_confines: List[main_models.GetRegionalInstanceConfigResponseBodyResultMasterDiskListSubClassificationConfines] = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit
        self.sub_classification_confines = sub_classification_confines

    def validate(self):
        if self.sub_classification_confines:
            for v1 in self.sub_classification_confines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit

        result['subClassificationConfines'] = []
        if self.sub_classification_confines is not None:
            for k1 in self.sub_classification_confines:
                result['subClassificationConfines'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')

        self.sub_classification_confines = []
        if m.get('subClassificationConfines') is not None:
            for k1 in m.get('subClassificationConfines'):
                temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultMasterDiskListSubClassificationConfines()
                self.sub_classification_confines.append(temp_model.from_map(k1))

        return self

class GetRegionalInstanceConfigResponseBodyResultMasterDiskListSubClassificationConfines(DaraModel):
    def __init__(
        self,
        max_size: int = None,
        min_size: int = None,
        performance_level: str = None,
    ):
        self.max_size = max_size
        self.min_size = min_size
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')

        return self

class GetRegionalInstanceConfigResponseBodyResultDataNodeDiskList(DaraModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
        sub_classification_confines: List[main_models.GetRegionalInstanceConfigResponseBodyResultDataNodeDiskListSubClassificationConfines] = None,
        value_limit_set: List[int] = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit
        self.sub_classification_confines = sub_classification_confines
        self.value_limit_set = value_limit_set

    def validate(self):
        if self.sub_classification_confines:
            for v1 in self.sub_classification_confines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit

        result['subClassificationConfines'] = []
        if self.sub_classification_confines is not None:
            for k1 in self.sub_classification_confines:
                result['subClassificationConfines'].append(k1.to_map() if k1 else None)

        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')

        self.sub_classification_confines = []
        if m.get('subClassificationConfines') is not None:
            for k1 in m.get('subClassificationConfines'):
                temp_model = main_models.GetRegionalInstanceConfigResponseBodyResultDataNodeDiskListSubClassificationConfines()
                self.sub_classification_confines.append(temp_model.from_map(k1))

        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')

        return self

class GetRegionalInstanceConfigResponseBodyResultDataNodeDiskListSubClassificationConfines(DaraModel):
    def __init__(
        self,
        max_size: int = None,
        min_size: int = None,
        performance_level: str = None,
    ):
        self.max_size = max_size
        self.min_size = min_size
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')

        return self

class GetRegionalInstanceConfigResponseBodyResultDataNodeAmountRange(DaraModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount

        if self.min_amount is not None:
            result['minAmount'] = self.min_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')

        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')

        return self

class GetRegionalInstanceConfigResponseBodyResultClientNodeDiskList(DaraModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')

        return self

class GetRegionalInstanceConfigResponseBodyResultClientNodeAmountRange(DaraModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount

        if self.min_amount is not None:
            result['minAmount'] = self.min_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')

        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')

        return self

