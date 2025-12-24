# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainLimitResponseBody(DaraModel):
    def __init__(
        self,
        live_domain_limit_list: main_models.DescribeLiveDomainLimitResponseBodyLiveDomainLimitList = None,
        request_id: str = None,
    ):
        # The limits.
        self.live_domain_limit_list = live_domain_limit_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_domain_limit_list:
            self.live_domain_limit_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_domain_limit_list is not None:
            result['LiveDomainLimitList'] = self.live_domain_limit_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveDomainLimitList') is not None:
            temp_model = main_models.DescribeLiveDomainLimitResponseBodyLiveDomainLimitList()
            self.live_domain_limit_list = temp_model.from_map(m.get('LiveDomainLimitList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDomainLimitResponseBodyLiveDomainLimitList(DaraModel):
    def __init__(
        self,
        live_domain_limit: List[main_models.DescribeLiveDomainLimitResponseBodyLiveDomainLimitListLiveDomainLimit] = None,
    ):
        self.live_domain_limit = live_domain_limit

    def validate(self):
        if self.live_domain_limit:
            for v1 in self.live_domain_limit:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveDomainLimit'] = []
        if self.live_domain_limit is not None:
            for k1 in self.live_domain_limit:
                result['LiveDomainLimit'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_domain_limit = []
        if m.get('LiveDomainLimit') is not None:
            for k1 in m.get('LiveDomainLimit'):
                temp_model = main_models.DescribeLiveDomainLimitResponseBodyLiveDomainLimitListLiveDomainLimit()
                self.live_domain_limit.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainLimitResponseBodyLiveDomainLimitListLiveDomainLimit(DaraModel):
    def __init__(
        self,
        current_num: int = None,
        current_transcode_num: int = None,
        current_transfer_num: int = None,
        domain_name: str = None,
        limit_num: int = None,
        limit_transcode_num: int = None,
        limit_transfer_num: int = None,
    ):
        # The current number of ingested streams.
        self.current_num = current_num
        # The current number of transcoded streams.
        self.current_transcode_num = current_transcode_num
        # The current number of streams relayed from the live center.
        self.current_transfer_num = current_transfer_num
        # The name of the queried main streaming domain.
        self.domain_name = domain_name
        # The maximum number of ingested streams.
        self.limit_num = limit_num
        # The maximum number of transcoded streams.
        self.limit_transcode_num = limit_transcode_num
        # The maximum allowed number of streams relayed from the live center.
        self.limit_transfer_num = limit_transfer_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_num is not None:
            result['CurrentNum'] = self.current_num

        if self.current_transcode_num is not None:
            result['CurrentTranscodeNum'] = self.current_transcode_num

        if self.current_transfer_num is not None:
            result['CurrentTransferNum'] = self.current_transfer_num

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.limit_num is not None:
            result['LimitNum'] = self.limit_num

        if self.limit_transcode_num is not None:
            result['LimitTranscodeNum'] = self.limit_transcode_num

        if self.limit_transfer_num is not None:
            result['LimitTransferNum'] = self.limit_transfer_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentNum') is not None:
            self.current_num = m.get('CurrentNum')

        if m.get('CurrentTranscodeNum') is not None:
            self.current_transcode_num = m.get('CurrentTranscodeNum')

        if m.get('CurrentTransferNum') is not None:
            self.current_transfer_num = m.get('CurrentTransferNum')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('LimitNum') is not None:
            self.limit_num = m.get('LimitNum')

        if m.get('LimitTranscodeNum') is not None:
            self.limit_transcode_num = m.get('LimitTranscodeNum')

        if m.get('LimitTransferNum') is not None:
            self.limit_transfer_num = m.get('LimitTransferNum')

        return self

