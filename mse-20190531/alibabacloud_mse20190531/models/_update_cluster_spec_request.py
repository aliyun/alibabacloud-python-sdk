# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateClusterSpecRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        auto_pay: bool = None,
        cluster_id: str = None,
        cluster_specification: str = None,
        instance_count: int = None,
        instance_id: str = None,
        mse_version: str = None,
        pub_network_flow: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        self.auto_pay = auto_pay
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The destination engine specifications.
        self.cluster_specification = cluster_specification
        # The number of destination nodes.
        self.instance_count = instance_count
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The MSE version.
        self.mse_version = mse_version
        self.pub_network_flow = pub_network_flow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version

        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')

        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')

        return self

