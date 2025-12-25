# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetWafQuotaResponseBody(DaraModel):
    def __init__(
        self,
        quota: main_models.GetWafQuotaResponseBodyQuota = None,
        request_id: str = None,
    ):
        # Returned quota information.
        self.quota = quota
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            temp_model = main_models.GetWafQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetWafQuotaResponseBodyQuota(DaraModel):
    def __init__(
        self,
        captcha: main_models.GetWafQuotaResponseBodyQuotaCaptcha = None,
        list: main_models.GetWafQuotaResponseBodyQuotaList = None,
        managed_rules_group: main_models.GetWafQuotaResponseBodyQuotaManagedRulesGroup = None,
        page: main_models.GetWafQuotaResponseBodyQuotaPage = None,
        scene_policy: main_models.GetWafQuotaResponseBodyQuotaScenePolicy = None,
    ):
        self.captcha = captcha
        # Quota information related to custom lists.
        self.list = list
        # Quota information related to the WAF managed rules group.
        self.managed_rules_group = managed_rules_group
        # Quota information related to custom response pages.
        self.page = page
        # Quota information related to scene protection.
        self.scene_policy = scene_policy

    def validate(self):
        if self.captcha:
            self.captcha.validate()
        if self.list:
            self.list.validate()
        if self.managed_rules_group:
            self.managed_rules_group.validate()
        if self.page:
            self.page.validate()
        if self.scene_policy:
            self.scene_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.captcha is not None:
            result['Captcha'] = self.captcha.to_map()

        if self.list is not None:
            result['List'] = self.list.to_map()

        if self.managed_rules_group is not None:
            result['ManagedRulesGroup'] = self.managed_rules_group.to_map()

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.scene_policy is not None:
            result['ScenePolicy'] = self.scene_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Captcha') is not None:
            temp_model = main_models.GetWafQuotaResponseBodyQuotaCaptcha()
            self.captcha = temp_model.from_map(m.get('Captcha'))

        if m.get('List') is not None:
            temp_model = main_models.GetWafQuotaResponseBodyQuotaList()
            self.list = temp_model.from_map(m.get('List'))

        if m.get('ManagedRulesGroup') is not None:
            temp_model = main_models.GetWafQuotaResponseBodyQuotaManagedRulesGroup()
            self.managed_rules_group = temp_model.from_map(m.get('ManagedRulesGroup'))

        if m.get('Page') is not None:
            temp_model = main_models.GetWafQuotaResponseBodyQuotaPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('ScenePolicy') is not None:
            temp_model = main_models.GetWafQuotaResponseBodyQuotaScenePolicy()
            self.scene_policy = temp_model.from_map(m.get('ScenePolicy'))

        return self

class GetWafQuotaResponseBodyQuotaScenePolicy(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        number_total: main_models.WafQuotaInteger = None,
    ):
        # Indicates whether the scene protection feature is enabled.
        self.enable = enable
        # The total number quota for scene protection rules.
        self.number_total = number_total

    def validate(self):
        if self.number_total:
            self.number_total.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.number_total is not None:
            result['NumberTotal'] = self.number_total.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('NumberTotal') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.number_total = temp_model.from_map(m.get('NumberTotal'))

        return self

class GetWafQuotaResponseBodyQuotaPage(DaraModel):
    def __init__(
        self,
        content_types: Dict[str, main_models.QuotaPageContentTypesValue] = None,
        enable: bool = None,
        number_total: main_models.WafQuotaInteger = None,
    ):
        # An object containing quota information for each Content-Type in custom response pages.
        self.content_types = content_types
        # Indicates whether the custom response page is enabled.
        self.enable = enable
        # The total number quota allowed for custom response pages.
        self.number_total = number_total

    def validate(self):
        if self.content_types:
            for v1 in self.content_types.values():
                 if v1:
                    v1.validate()
        if self.number_total:
            self.number_total.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContentTypes'] = {}
        if self.content_types is not None:
            for k1, v1 in self.content_types.items():
                result['ContentTypes'][k1] = v1.to_map() if v1 else None

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.number_total is not None:
            result['NumberTotal'] = self.number_total.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content_types = {}
        if m.get('ContentTypes') is not None:
            for k1, v1 in m.get('ContentTypes').items():
                temp_model = main_models.QuotaPageContentTypesValue()
                self.content_types[k1] = temp_model.from_map(v1)

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('NumberTotal') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.number_total = temp_model.from_map(m.get('NumberTotal'))

        return self

class GetWafQuotaResponseBodyQuotaManagedRulesGroup(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        number_total: main_models.WafQuotaInteger = None,
    ):
        # Indicates whether the WAF managed rules group is enabled.
        self.enable = enable
        # The total number quota allowed for the WAF managed rules group.
        self.number_total = number_total

    def validate(self):
        if self.number_total:
            self.number_total.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.number_total is not None:
            result['NumberTotal'] = self.number_total.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('NumberTotal') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.number_total = temp_model.from_map(m.get('NumberTotal'))

        return self

class GetWafQuotaResponseBodyQuotaList(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        items: Dict[str, main_models.QuotaListItemsValue] = None,
        number_items_per_list: main_models.WafQuotaInteger = None,
        number_items_total: main_models.WafQuotaInteger = None,
        number_total: main_models.WafQuotaInteger = None,
    ):
        # Indicates whether the custom list is enabled.
        self.enable = enable
        # An object containing quota information for each type of item in the custom list.
        self.items = items
        # The number quota allowed per custom list.
        self.number_items_per_list = number_items_per_list
        # The total number quota allowed for items in all custom lists.
        self.number_items_total = number_items_total
        # The total number quota allowed for custom lists.
        self.number_total = number_total

    def validate(self):
        if self.items:
            for v1 in self.items.values():
                 if v1:
                    v1.validate()
        if self.number_items_per_list:
            self.number_items_per_list.validate()
        if self.number_items_total:
            self.number_items_total.validate()
        if self.number_total:
            self.number_total.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        result['Items'] = {}
        if self.items is not None:
            for k1, v1 in self.items.items():
                result['Items'][k1] = v1.to_map() if v1 else None

        if self.number_items_per_list is not None:
            result['NumberItemsPerList'] = self.number_items_per_list.to_map()

        if self.number_items_total is not None:
            result['NumberItemsTotal'] = self.number_items_total.to_map()

        if self.number_total is not None:
            result['NumberTotal'] = self.number_total.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        self.items = {}
        if m.get('Items') is not None:
            for k1, v1 in m.get('Items').items():
                temp_model = main_models.QuotaListItemsValue()
                self.items[k1] = temp_model.from_map(v1)

        if m.get('NumberItemsPerList') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.number_items_per_list = temp_model.from_map(m.get('NumberItemsPerList'))

        if m.get('NumberItemsTotal') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.number_items_total = temp_model.from_map(m.get('NumberItemsTotal'))

        if m.get('NumberTotal') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.number_total = temp_model.from_map(m.get('NumberTotal'))

        return self

class GetWafQuotaResponseBodyQuotaCaptcha(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        number_total: main_models.WafQuotaInteger = None,
    ):
        self.enable = enable
        self.number_total = number_total

    def validate(self):
        if self.number_total:
            self.number_total.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.number_total is not None:
            result['NumberTotal'] = self.number_total.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('NumberTotal') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.number_total = temp_model.from_map(m.get('NumberTotal'))

        return self

