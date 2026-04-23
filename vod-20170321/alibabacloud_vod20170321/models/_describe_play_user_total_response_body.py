# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribePlayUserTotalResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_play_statis_totals: main_models.DescribePlayUserTotalResponseBodyUserPlayStatisTotals = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.user_play_statis_totals = user_play_statis_totals

    def validate(self):
        if self.user_play_statis_totals:
            self.user_play_statis_totals.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_play_statis_totals is not None:
            result['UserPlayStatisTotals'] = self.user_play_statis_totals.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserPlayStatisTotals') is not None:
            temp_model = main_models.DescribePlayUserTotalResponseBodyUserPlayStatisTotals()
            self.user_play_statis_totals = temp_model.from_map(m.get('UserPlayStatisTotals'))

        return self

class DescribePlayUserTotalResponseBodyUserPlayStatisTotals(DaraModel):
    def __init__(
        self,
        user_play_statis_total: List[main_models.DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotal] = None,
    ):
        self.user_play_statis_total = user_play_statis_total

    def validate(self):
        if self.user_play_statis_total:
            for v1 in self.user_play_statis_total:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserPlayStatisTotal'] = []
        if self.user_play_statis_total is not None:
            for k1 in self.user_play_statis_total:
                result['UserPlayStatisTotal'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_play_statis_total = []
        if m.get('UserPlayStatisTotal') is not None:
            for k1 in m.get('UserPlayStatisTotal'):
                temp_model = main_models.DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotal()
                self.user_play_statis_total.append(temp_model.from_map(k1))

        return self

class DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotal(DaraModel):
    def __init__(
        self,
        date: str = None,
        play_duration: str = None,
        play_range: str = None,
        uv: main_models.DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV = None,
        vv: main_models.DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV = None,
    ):
        self.date = date
        self.play_duration = play_duration
        self.play_range = play_range
        self.uv = uv
        self.vv = vv

    def validate(self):
        if self.uv:
            self.uv.validate()
        if self.vv:
            self.vv.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration

        if self.play_range is not None:
            result['PlayRange'] = self.play_range

        if self.uv is not None:
            result['UV'] = self.uv.to_map()

        if self.vv is not None:
            result['VV'] = self.vv.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')

        if m.get('PlayRange') is not None:
            self.play_range = m.get('PlayRange')

        if m.get('UV') is not None:
            temp_model = main_models.DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV()
            self.uv = temp_model.from_map(m.get('UV'))

        if m.get('VV') is not None:
            temp_model = main_models.DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV()
            self.vv = temp_model.from_map(m.get('VV'))

        return self

class DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV(DaraModel):
    def __init__(
        self,
        android: str = None,
        flash: str = None,
        html5: str = None,
        i_os: str = None,
    ):
        self.android = android
        self.flash = flash
        self.html5 = html5
        self.i_os = i_os

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android is not None:
            result['Android'] = self.android

        if self.flash is not None:
            result['Flash'] = self.flash

        if self.html5 is not None:
            result['HTML5'] = self.html5

        if self.i_os is not None:
            result['iOS'] = self.i_os

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Android') is not None:
            self.android = m.get('Android')

        if m.get('Flash') is not None:
            self.flash = m.get('Flash')

        if m.get('HTML5') is not None:
            self.html5 = m.get('HTML5')

        if m.get('iOS') is not None:
            self.i_os = m.get('iOS')

        return self

class DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV(DaraModel):
    def __init__(
        self,
        android: str = None,
        flash: str = None,
        html5: str = None,
        i_os: str = None,
    ):
        self.android = android
        self.flash = flash
        self.html5 = html5
        self.i_os = i_os

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android is not None:
            result['Android'] = self.android

        if self.flash is not None:
            result['Flash'] = self.flash

        if self.html5 is not None:
            result['HTML5'] = self.html5

        if self.i_os is not None:
            result['iOS'] = self.i_os

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Android') is not None:
            self.android = m.get('Android')

        if m.get('Flash') is not None:
            self.flash = m.get('Flash')

        if m.get('HTML5') is not None:
            self.html5 = m.get('HTML5')

        if m.get('iOS') is not None:
            self.i_os = m.get('iOS')

        return self

