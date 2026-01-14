# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartClusterRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        instance_id: str = None,
        pod_name_list: str = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The names of pods. You can specify the names of multiple pods at a time. Separate multiple pod names with commas (,). Example: mse-a8aba010-1629719288255-reg-center-0-1,mse-a8aba010-1629719288255-reg-center-0-2.
        # 
        # The specified pods must belong to the current cluster and be associated with the specified instance. Otherwise, a restart exception occurs.
        self.pod_name_list = pod_name_list
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

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pod_name_list is not None:
            result['PodNameList'] = self.pod_name_list

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PodNameList') is not None:
            self.pod_name_list = m.get('PodNameList')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

