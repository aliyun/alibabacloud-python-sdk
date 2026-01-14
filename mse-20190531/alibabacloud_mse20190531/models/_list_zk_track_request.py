# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListZkTrackRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        end_ts: int = None,
        instance_id: str = None,
        page_num: int = None,
        page_size: int = None,
        path: str = None,
        request_pars: str = None,
        reverse: bool = None,
        session_id: str = None,
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The path.
        self.path = path
        # The request parameters.
        self.request_pars = request_pars
        # Specifies whether to enable reverse ordering.
        self.reverse = reverse
        # The session ID.
        self.session_id = session_id
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        return self

