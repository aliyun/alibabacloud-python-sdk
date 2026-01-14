# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClusterVersionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_type: str = None,
        mse_version: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The type of the instance. Valid values: ZooKeeper, Nacos-Ans, and Eureka.
        self.cluster_type = cluster_type
        # The instance edition. Valid values:
        # 
        # *   `mse_dev`: Developer Edition.
        # *   `mse_pro`: Professional Edition. This is the default value.
        self.mse_version = mse_version

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')

        return self

