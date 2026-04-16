# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudUpdateTaskResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudUpdateTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CloudUpdateTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudUpdateTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_timeout: str = None,
        answer_rate: str = None,
        auto_complete: int = None,
        auto_start: str = None,
        auto_start_day: str = None,
        auto_start_time: str = None,
        auto_stop: str = None,
        auto_stop_day: str = None,
        auto_stop_time: str = None,
        cnos: str = None,
        concurrency: str = None,
        create_time: str = None,
        customer_clids: str = None,
        customer_moh: str = None,
        customer_timeout: str = None,
        description: str = None,
        enterprise_id: str = None,
        id: str = None,
        is_random: str = None,
        ivr_id: str = None,
        max_wait_time: str = None,
        name: str = None,
        over_time: str = None,
        predict_adjust: str = None,
        quotiety: str = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
        user_fields: str = None,
        wrapup: str = None,
    ):
        self.agent_timeout = agent_timeout
        self.answer_rate = answer_rate
        self.auto_complete = auto_complete
        self.auto_start = auto_start
        self.auto_start_day = auto_start_day
        self.auto_start_time = auto_start_time
        self.auto_stop = auto_stop
        self.auto_stop_day = auto_stop_day
        self.auto_stop_time = auto_stop_time
        self.cnos = cnos
        self.concurrency = concurrency
        self.create_time = create_time
        self.customer_clids = customer_clids
        self.customer_moh = customer_moh
        self.customer_timeout = customer_timeout
        self.description = description
        self.enterprise_id = enterprise_id
        self.id = id
        self.is_random = is_random
        self.ivr_id = ivr_id
        self.max_wait_time = max_wait_time
        self.name = name
        self.over_time = over_time
        self.predict_adjust = predict_adjust
        self.quotiety = quotiety
        self.start_time = start_time
        self.status = status
        self.type = type
        self.user_fields = user_fields
        self.wrapup = wrapup

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_timeout is not None:
            result['AgentTimeout'] = self.agent_timeout

        if self.answer_rate is not None:
            result['AnswerRate'] = self.answer_rate

        if self.auto_complete is not None:
            result['AutoComplete'] = self.auto_complete

        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start

        if self.auto_start_day is not None:
            result['AutoStartDay'] = self.auto_start_day

        if self.auto_start_time is not None:
            result['AutoStartTime'] = self.auto_start_time

        if self.auto_stop is not None:
            result['AutoStop'] = self.auto_stop

        if self.auto_stop_day is not None:
            result['AutoStopDay'] = self.auto_stop_day

        if self.auto_stop_time is not None:
            result['AutoStopTime'] = self.auto_stop_time

        if self.cnos is not None:
            result['Cnos'] = self.cnos

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.customer_clids is not None:
            result['CustomerClids'] = self.customer_clids

        if self.customer_moh is not None:
            result['CustomerMoh'] = self.customer_moh

        if self.customer_timeout is not None:
            result['CustomerTimeout'] = self.customer_timeout

        if self.description is not None:
            result['Description'] = self.description

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.id is not None:
            result['Id'] = self.id

        if self.is_random is not None:
            result['IsRandom'] = self.is_random

        if self.ivr_id is not None:
            result['IvrId'] = self.ivr_id

        if self.max_wait_time is not None:
            result['MaxWaitTime'] = self.max_wait_time

        if self.name is not None:
            result['Name'] = self.name

        if self.over_time is not None:
            result['OverTime'] = self.over_time

        if self.predict_adjust is not None:
            result['PredictAdjust'] = self.predict_adjust

        if self.quotiety is not None:
            result['Quotiety'] = self.quotiety

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.user_fields is not None:
            result['UserFields'] = self.user_fields

        if self.wrapup is not None:
            result['Wrapup'] = self.wrapup

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentTimeout') is not None:
            self.agent_timeout = m.get('AgentTimeout')

        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')

        if m.get('AutoComplete') is not None:
            self.auto_complete = m.get('AutoComplete')

        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')

        if m.get('AutoStartDay') is not None:
            self.auto_start_day = m.get('AutoStartDay')

        if m.get('AutoStartTime') is not None:
            self.auto_start_time = m.get('AutoStartTime')

        if m.get('AutoStop') is not None:
            self.auto_stop = m.get('AutoStop')

        if m.get('AutoStopDay') is not None:
            self.auto_stop_day = m.get('AutoStopDay')

        if m.get('AutoStopTime') is not None:
            self.auto_stop_time = m.get('AutoStopTime')

        if m.get('Cnos') is not None:
            self.cnos = m.get('Cnos')

        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomerClids') is not None:
            self.customer_clids = m.get('CustomerClids')

        if m.get('CustomerMoh') is not None:
            self.customer_moh = m.get('CustomerMoh')

        if m.get('CustomerTimeout') is not None:
            self.customer_timeout = m.get('CustomerTimeout')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsRandom') is not None:
            self.is_random = m.get('IsRandom')

        if m.get('IvrId') is not None:
            self.ivr_id = m.get('IvrId')

        if m.get('MaxWaitTime') is not None:
            self.max_wait_time = m.get('MaxWaitTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OverTime') is not None:
            self.over_time = m.get('OverTime')

        if m.get('PredictAdjust') is not None:
            self.predict_adjust = m.get('PredictAdjust')

        if m.get('Quotiety') is not None:
            self.quotiety = m.get('Quotiety')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserFields') is not None:
            self.user_fields = m.get('UserFields')

        if m.get('Wrapup') is not None:
            self.wrapup = m.get('Wrapup')

        return self

