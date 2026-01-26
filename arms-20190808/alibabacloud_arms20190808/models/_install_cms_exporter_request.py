# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallCmsExporterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cms_args: str = None,
        direct_args: str = None,
        enable_tag: bool = None,
        region_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The cloud services that you want to monitor. The CmsArgs parameter is the startup parameter of the cms-exporter collector. Separate multiple cloud services with number signs (`#`).
        self.cms_args = cms_args
        # The recently monitored cloud services. Separate multiple cloud services with number signs (`#`).
        self.direct_args = direct_args
        # Specifies whether to collect the aliyun tags attached to each cloud service. Default value: false.
        self.enable_tag = enable_tag
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cms_args is not None:
            result['CmsArgs'] = self.cms_args

        if self.direct_args is not None:
            result['DirectArgs'] = self.direct_args

        if self.enable_tag is not None:
            result['EnableTag'] = self.enable_tag

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CmsArgs') is not None:
            self.cms_args = m.get('CmsArgs')

        if m.get('DirectArgs') is not None:
            self.direct_args = m.get('DirectArgs')

        if m.get('EnableTag') is not None:
            self.enable_tag = m.get('EnableTag')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

