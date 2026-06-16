# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_antiddos_public20170518 import models as main_models
from darabonba.model import DaraModel

class DescribeDdosCreditResponseBody(DaraModel):
    def __init__(
        self,
        ddos_credit: main_models.DescribeDdosCreditResponseBodyDdosCredit = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the security credit score of the current Alibaba Cloud account in the specified region.
        self.ddos_credit = ddos_credit
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: yes
        # 
        # - **false**: no
        self.success = success

    def validate(self):
        if self.ddos_credit:
            self.ddos_credit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_credit is not None:
            result['DdosCredit'] = self.ddos_credit.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosCredit') is not None:
            temp_model = main_models.DescribeDdosCreditResponseBodyDdosCredit()
            self.ddos_credit = temp_model.from_map(m.get('DdosCredit'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDdosCreditResponseBodyDdosCredit(DaraModel):
    def __init__(
        self,
        blackhole_time: int = None,
        score: int = None,
        score_level: str = None,
    ):
        # The time period after which blackhole filtering is automatically deactivated in the specified region. Unit: minutes.
        self.blackhole_time = blackhole_time
        # The security credit score. The full score is **1000**.
        self.score = score
        # The security credit level. Valid values:
        # 
        # - **A**: outstanding
        # 
        # - **B**: excellent
        # 
        # - **C**: good
        # 
        # - **D**: average
        # 
        # - **E**: poor
        # 
        # - **F**: poorer
        self.score_level = score_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blackhole_time is not None:
            result['BlackholeTime'] = self.blackhole_time

        if self.score is not None:
            result['Score'] = self.score

        if self.score_level is not None:
            result['ScoreLevel'] = self.score_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackholeTime') is not None:
            self.blackhole_time = m.get('BlackholeTime')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ScoreLevel') is not None:
            self.score_level = m.get('ScoreLevel')

        return self

