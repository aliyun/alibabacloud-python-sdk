# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PocSendDataRequest(DaraModel):
    def __init__(
        self,
        batch_no: int = None,
        lang: str = None,
        params_list: str = None,
        reg_id: str = None,
        token: str = None,
    ):
        # Starting position for batch operations, starting from 0.
        # 
        # This parameter is required.
        self.batch_no = batch_no
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Return parameters, in JSON format.
        # 
        # This parameter is required.
        self.params_list = params_list
        # Region code.
        self.reg_id = reg_id
        # Task token.
        # 
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_no is not None:
            result['BatchNo'] = self.batch_no

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.params_list is not None:
            result['ParamsList'] = self.params_list

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchNo') is not None:
            self.batch_no = m.get('BatchNo')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ParamsList') is not None:
            self.params_list = m.get('ParamsList')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

