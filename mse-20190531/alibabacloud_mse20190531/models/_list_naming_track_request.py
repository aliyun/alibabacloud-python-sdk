# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNamingTrackRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        end_ts: int = None,
        group: str = None,
        instance_id: str = None,
        ip: str = None,
        namespace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        request_pars: str = None,
        reverse: bool = None,
        service_name: str = None,
        start_ts: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The end timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_ts = end_ts
        # The group.
        self.group = group
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IP address of the client.
        self.ip = ip
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars
        # Specifies whether to sort the query results in chronological order or reverse chronological order. Default value: `false`.
        # 
        # *   `true`: sorts the query results in reverse chronological order.
        # *   `false`: sorts the query results in chronological order.
        self.reverse = reverse
        # The name of the service.
        self.service_name = service_name
        # The start timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        return self

