# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAllImageBaselineResponseBody(DaraModel):
    def __init__(
        self,
        image_baselines: main_models.DescribeAllImageBaselineResponseBodyImageBaselines = None,
        request_id: str = None,
    ):
        # The baselines that are used in image baseline checks.
        self.image_baselines = image_baselines
        # The ID of the request, which is used to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.image_baselines:
            self.image_baselines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_baselines is not None:
            result['ImageBaselines'] = self.image_baselines.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageBaselines') is not None:
            temp_model = main_models.DescribeAllImageBaselineResponseBodyImageBaselines()
            self.image_baselines = temp_model.from_map(m.get('ImageBaselines'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAllImageBaselineResponseBodyImageBaselines(DaraModel):
    def __init__(
        self,
        baseline_class_list: List[main_models.DescribeAllImageBaselineResponseBodyImageBaselinesBaselineClassList] = None,
    ):
        # An array that consists of baseline types.
        self.baseline_class_list = baseline_class_list

    def validate(self):
        if self.baseline_class_list:
            for v1 in self.baseline_class_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaselineClassList'] = []
        if self.baseline_class_list is not None:
            for k1 in self.baseline_class_list:
                result['BaselineClassList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline_class_list = []
        if m.get('BaselineClassList') is not None:
            for k1 in m.get('BaselineClassList'):
                temp_model = main_models.DescribeAllImageBaselineResponseBodyImageBaselinesBaselineClassList()
                self.baseline_class_list.append(temp_model.from_map(k1))

        return self

class DescribeAllImageBaselineResponseBodyImageBaselinesBaselineClassList(DaraModel):
    def __init__(
        self,
        alias: str = None,
        baseline_name_list: List[main_models.DescribeAllImageBaselineResponseBodyImageBaselinesBaselineClassListBaselineNameList] = None,
        class_key: str = None,
    ):
        # The alias of the baseline type.
        self.alias = alias
        # The information about the baseline.
        self.baseline_name_list = baseline_name_list
        # The key of the baseline type.
        self.class_key = class_key

    def validate(self):
        if self.baseline_name_list:
            for v1 in self.baseline_name_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        result['BaselineNameList'] = []
        if self.baseline_name_list is not None:
            for k1 in self.baseline_name_list:
                result['BaselineNameList'].append(k1.to_map() if k1 else None)

        if self.class_key is not None:
            result['ClassKey'] = self.class_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        self.baseline_name_list = []
        if m.get('BaselineNameList') is not None:
            for k1 in m.get('BaselineNameList'):
                temp_model = main_models.DescribeAllImageBaselineResponseBodyImageBaselinesBaselineClassListBaselineNameList()
                self.baseline_name_list.append(temp_model.from_map(k1))

        if m.get('ClassKey') is not None:
            self.class_key = m.get('ClassKey')

        return self

class DescribeAllImageBaselineResponseBodyImageBaselinesBaselineClassListBaselineNameList(DaraModel):
    def __init__(
        self,
        alias: str = None,
        baseline_item_list: List[main_models.DescribeAllImageBaselineResponseBodyImageBaselinesBaselineClassListBaselineNameListBaselineItemList] = None,
        class_key: str = None,
        name_key: str = None,
    ):
        # The alias of the baseline.
        self.alias = alias
        # The information about the baseline check item.
        self.baseline_item_list = baseline_item_list
        # The key of the type for the baseline.
        self.class_key = class_key
        # The key of the name for the baseline.
        self.name_key = name_key

    def validate(self):
        if self.baseline_item_list:
            for v1 in self.baseline_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        result['BaselineItemList'] = []
        if self.baseline_item_list is not None:
            for k1 in self.baseline_item_list:
                result['BaselineItemList'].append(k1.to_map() if k1 else None)

        if self.class_key is not None:
            result['ClassKey'] = self.class_key

        if self.name_key is not None:
            result['NameKey'] = self.name_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        self.baseline_item_list = []
        if m.get('BaselineItemList') is not None:
            for k1 in m.get('BaselineItemList'):
                temp_model = main_models.DescribeAllImageBaselineResponseBodyImageBaselinesBaselineClassListBaselineNameListBaselineItemList()
                self.baseline_item_list.append(temp_model.from_map(k1))

        if m.get('ClassKey') is not None:
            self.class_key = m.get('ClassKey')

        if m.get('NameKey') is not None:
            self.name_key = m.get('NameKey')

        return self

class DescribeAllImageBaselineResponseBodyImageBaselinesBaselineClassListBaselineNameListBaselineItemList(DaraModel):
    def __init__(
        self,
        alias: str = None,
        class_key: str = None,
        item_key: str = None,
        name_key: str = None,
    ):
        # The alias of the baseline check item.
        self.alias = alias
        # The key of the type for the baseline.
        self.class_key = class_key
        # The key of the name for the baseline check item.
        self.item_key = item_key
        # The key of the name for the baseline.
        self.name_key = name_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.class_key is not None:
            result['ClassKey'] = self.class_key

        if self.item_key is not None:
            result['ItemKey'] = self.item_key

        if self.name_key is not None:
            result['NameKey'] = self.name_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('ClassKey') is not None:
            self.class_key = m.get('ClassKey')

        if m.get('ItemKey') is not None:
            self.item_key = m.get('ItemKey')

        if m.get('NameKey') is not None:
            self.name_key = m.get('NameKey')

        return self

