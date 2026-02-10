# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCheckStandardRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        instance_sub_types: List[str] = None,
        instance_types: List[str] = None,
        lang: str = None,
        task_sources: List[str] = None,
        vendors: List[str] = None,
    ):
        # The instance IDs of the cloud services to which the check items belong.
        self.instance_ids = instance_ids
        # The subtypes of cloud services.
        self.instance_sub_types = instance_sub_types
        # The asset types of cloud services.
        self.instance_types = instance_types
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # List of task sources.
        self.task_sources = task_sources
        # The cloud service providers. Valid values:
        # 
        # *   **ALIYUN**: Alibaba Cloud.
        # *   **TENCENT**: Tencent Cloud.
        # *   **HUAWEICLOUD**: Huawei Cloud.
        # *   **MICROSOFT**: Microsoft Azure.
        # *   **AWS**: Amazon Web Services (AWS).
        self.vendors = vendors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_sub_types is not None:
            result['InstanceSubTypes'] = self.instance_sub_types

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.task_sources is not None:
            result['TaskSources'] = self.task_sources

        if self.vendors is not None:
            result['Vendors'] = self.vendors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceSubTypes') is not None:
            self.instance_sub_types = m.get('InstanceSubTypes')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TaskSources') is not None:
            self.task_sources = m.get('TaskSources')

        if m.get('Vendors') is not None:
            self.vendors = m.get('Vendors')

        return self

