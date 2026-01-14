# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceCountRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_type: str = None,
        mse_version: str = None,
        region_id: str = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The type of the instance. Valid values: ZooKeeper and Nacos-Ans.
        self.cluster_type = cluster_type
        # The edition type of the instance. Valid values:
        # 
        # *   `mse_dev`: Developer Edition
        # *   `mse_pro`: Professional Edition
        self.mse_version = mse_version
        # The ID of the region where the instance resides. Examples:
        # 
        # *   cn-hangzhou: China (Hangzhou)
        # *   cn-beijing: China (Beijing)
        # *   cn-shanghai: China (Shanghai)
        # *   cn-zhangjiakou: China (Zhangjiakou)
        # *   cn-shenzhen: China (Shenzhen)
        self.region_id = region_id
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

