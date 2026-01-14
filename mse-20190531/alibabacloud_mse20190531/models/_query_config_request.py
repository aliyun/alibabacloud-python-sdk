# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        config_type: str = None,
        instance_id: str = None,
        need_running_conf: bool = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # A reserved parameter.
        self.config_type = config_type
        # The ID of the instance.
        self.instance_id = instance_id
        # Specifies whether runtime configurations are required.
        self.need_running_conf = need_running_conf
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

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.need_running_conf is not None:
            result['NeedRunningConf'] = self.need_running_conf

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NeedRunningConf') is not None:
            self.need_running_conf = m.get('NeedRunningConf')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

