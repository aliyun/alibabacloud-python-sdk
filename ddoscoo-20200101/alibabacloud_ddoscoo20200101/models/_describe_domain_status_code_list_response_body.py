# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainStatusCodeListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status_code_list: List[main_models.DescribeDomainStatusCodeListResponseBodyStatusCodeList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The statistics on response status codes.
        self.status_code_list = status_code_list

    def validate(self):
        if self.status_code_list:
            for v1 in self.status_code_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StatusCodeList'] = []
        if self.status_code_list is not None:
            for k1 in self.status_code_list:
                result['StatusCodeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.status_code_list = []
        if m.get('StatusCodeList') is not None:
            for k1 in m.get('StatusCodeList'):
                temp_model = main_models.DescribeDomainStatusCodeListResponseBodyStatusCodeList()
                self.status_code_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainStatusCodeListResponseBodyStatusCodeList(DaraModel):
    def __init__(
        self,
        index: int = None,
        status_200: int = None,
        status_2xx: int = None,
        status_3xx: int = None,
        status_403: int = None,
        status_404: int = None,
        status_405: int = None,
        status_410: int = None,
        status_499: int = None,
        status_4xx: int = None,
        status_501: int = None,
        status_502: int = None,
        status_503: int = None,
        status_504: int = None,
        status_5xx: int = None,
        time: int = None,
    ):
        # The index number of the returned data.
        self.index = index
        # The number of 200 status codes.
        self.status_200 = status_200
        # The number of 2xx status codes.
        self.status_2xx = status_2xx
        # The number of 3xx status codes.
        self.status_3xx = status_3xx
        # The number of 403 status codes.
        self.status_403 = status_403
        # The number of 404 status codes.
        self.status_404 = status_404
        # The number of 405 status codes.
        self.status_405 = status_405
        self.status_410 = status_410
        self.status_499 = status_499
        # The number of 4xx status codes.
        self.status_4xx = status_4xx
        # The number of 501 status codes.
        self.status_501 = status_501
        # The number of 502 status codes.
        self.status_502 = status_502
        # The number of 503 status codes.
        self.status_503 = status_503
        # The number of 504 status codes.
        self.status_504 = status_504
        # The number of 5xx status codes.
        self.status_5xx = status_5xx
        # The time when the data was collected. The value is a UNIX timestamp. Unit: seconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.status_200 is not None:
            result['Status200'] = self.status_200

        if self.status_2xx is not None:
            result['Status2XX'] = self.status_2xx

        if self.status_3xx is not None:
            result['Status3XX'] = self.status_3xx

        if self.status_403 is not None:
            result['Status403'] = self.status_403

        if self.status_404 is not None:
            result['Status404'] = self.status_404

        if self.status_405 is not None:
            result['Status405'] = self.status_405

        if self.status_410 is not None:
            result['Status410'] = self.status_410

        if self.status_499 is not None:
            result['Status499'] = self.status_499

        if self.status_4xx is not None:
            result['Status4XX'] = self.status_4xx

        if self.status_501 is not None:
            result['Status501'] = self.status_501

        if self.status_502 is not None:
            result['Status502'] = self.status_502

        if self.status_503 is not None:
            result['Status503'] = self.status_503

        if self.status_504 is not None:
            result['Status504'] = self.status_504

        if self.status_5xx is not None:
            result['Status5XX'] = self.status_5xx

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Status200') is not None:
            self.status_200 = m.get('Status200')

        if m.get('Status2XX') is not None:
            self.status_2xx = m.get('Status2XX')

        if m.get('Status3XX') is not None:
            self.status_3xx = m.get('Status3XX')

        if m.get('Status403') is not None:
            self.status_403 = m.get('Status403')

        if m.get('Status404') is not None:
            self.status_404 = m.get('Status404')

        if m.get('Status405') is not None:
            self.status_405 = m.get('Status405')

        if m.get('Status410') is not None:
            self.status_410 = m.get('Status410')

        if m.get('Status499') is not None:
            self.status_499 = m.get('Status499')

        if m.get('Status4XX') is not None:
            self.status_4xx = m.get('Status4XX')

        if m.get('Status501') is not None:
            self.status_501 = m.get('Status501')

        if m.get('Status502') is not None:
            self.status_502 = m.get('Status502')

        if m.get('Status503') is not None:
            self.status_503 = m.get('Status503')

        if m.get('Status504') is not None:
            self.status_504 = m.get('Status504')

        if m.get('Status5XX') is not None:
            self.status_5xx = m.get('Status5XX')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

