# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DoLogicalDeleteResourceResponseBody(DaraModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        message: str = None,
        pk: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.message = message
        self.pk = pk
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['Bid'] = self.bid

        if self.country is not None:
            result['Country'] = self.country

        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup

        if self.hid is not None:
            result['Hid'] = self.hid

        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt

        if self.invoker is not None:
            result['Invoker'] = self.invoker

        if self.message is not None:
            result['Message'] = self.message

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.success is not None:
            result['Success'] = self.success

        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data

        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')

        if m.get('Hid') is not None:
            self.hid = m.get('Hid')

        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')

        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')

        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')

        return self

