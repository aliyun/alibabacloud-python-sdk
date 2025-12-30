# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class PreviewGtmRecoveryPlanResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        previews: main_models.PreviewGtmRecoveryPlanResponseBodyPreviews = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The returned preview information of the disaster recovery plan.
        self.previews = previews
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned on all pages.
        self.total_items = total_items
        # The total number of pages returned.
        self.total_pages = total_pages

    def validate(self):
        if self.previews:
            self.previews.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.previews is not None:
            result['Previews'] = self.previews.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Previews') is not None:
            temp_model = main_models.PreviewGtmRecoveryPlanResponseBodyPreviews()
            self.previews = temp_model.from_map(m.get('Previews'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class PreviewGtmRecoveryPlanResponseBodyPreviews(DaraModel):
    def __init__(
        self,
        preview: List[main_models.PreviewGtmRecoveryPlanResponseBodyPreviewsPreview] = None,
    ):
        self.preview = preview

    def validate(self):
        if self.preview:
            for v1 in self.preview:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Preview'] = []
        if self.preview is not None:
            for k1 in self.preview:
                result['Preview'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.preview = []
        if m.get('Preview') is not None:
            for k1 in m.get('Preview'):
                temp_model = main_models.PreviewGtmRecoveryPlanResponseBodyPreviewsPreview()
                self.preview.append(temp_model.from_map(k1))

        return self

class PreviewGtmRecoveryPlanResponseBodyPreviewsPreview(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        switch_infos: main_models.PreviewGtmRecoveryPlanResponseBodyPreviewsPreviewSwitchInfos = None,
        user_domain_name: str = None,
    ):
        # The ID of the GTM instance to which the previewed disaster recovery plan belongs.
        self.instance_id = instance_id
        # The name of the GTM instance to which the previewed disaster recovery plan belongs.
        self.name = name
        # The returned information of the switching policies for address pools.
        self.switch_infos = switch_infos
        # The user\\"s domain name or domain name list.
        self.user_domain_name = user_domain_name

    def validate(self):
        if self.switch_infos:
            self.switch_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.switch_infos is not None:
            result['SwitchInfos'] = self.switch_infos.to_map()

        if self.user_domain_name is not None:
            result['UserDomainName'] = self.user_domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SwitchInfos') is not None:
            temp_model = main_models.PreviewGtmRecoveryPlanResponseBodyPreviewsPreviewSwitchInfos()
            self.switch_infos = temp_model.from_map(m.get('SwitchInfos'))

        if m.get('UserDomainName') is not None:
            self.user_domain_name = m.get('UserDomainName')

        return self

class PreviewGtmRecoveryPlanResponseBodyPreviewsPreviewSwitchInfos(DaraModel):
    def __init__(
        self,
        switch_info: List[main_models.PreviewGtmRecoveryPlanResponseBodyPreviewsPreviewSwitchInfosSwitchInfo] = None,
    ):
        self.switch_info = switch_info

    def validate(self):
        if self.switch_info:
            for v1 in self.switch_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SwitchInfo'] = []
        if self.switch_info is not None:
            for k1 in self.switch_info:
                result['SwitchInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.switch_info = []
        if m.get('SwitchInfo') is not None:
            for k1 in m.get('SwitchInfo'):
                temp_model = main_models.PreviewGtmRecoveryPlanResponseBodyPreviewsPreviewSwitchInfosSwitchInfo()
                self.switch_info.append(temp_model.from_map(k1))

        return self

class PreviewGtmRecoveryPlanResponseBodyPreviewsPreviewSwitchInfosSwitchInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        strategy_name: str = None,
    ):
        # The formatted message content.
        self.content = content
        # The name of the switching policy for address pools.
        self.strategy_name = strategy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

