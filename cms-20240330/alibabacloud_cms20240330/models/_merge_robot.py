# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class MergeRobot(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        extend: main_models.MergeRobotExtend = None,
        gmt_modified: str = None,
        identifier: str = None,
        lang: str = None,
        name: str = None,
        source: str = None,
        type: str = None,
        webhook: str = None,
    ):
        self.create_time = create_time
        self.extend = extend
        self.gmt_modified = gmt_modified
        self.identifier = identifier
        self.lang = lang
        self.name = name
        self.source = source
        self.type = type
        self.webhook = webhook

    def validate(self):
        if self.extend:
            self.extend.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.extend is not None:
            result['extend'] = self.extend.to_map()

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.identifier is not None:
            result['identifier'] = self.identifier

        if self.lang is not None:
            result['lang'] = self.lang

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.type is not None:
            result['type'] = self.type

        if self.webhook is not None:
            result['webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('extend') is not None:
            temp_model = main_models.MergeRobotExtend()
            self.extend = temp_model.from_map(m.get('extend'))

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')

        return self

class MergeRobotExtend(DaraModel):
    def __init__(
        self,
        card_template: str = None,
        daily_noc: bool = None,
        daily_noc_time: str = None,
        ding_sign_key: str = None,
        enable_outgoing: bool = None,
        token: str = None,
    ):
        self.card_template = card_template
        self.daily_noc = daily_noc
        self.daily_noc_time = daily_noc_time
        self.ding_sign_key = ding_sign_key
        self.enable_outgoing = enable_outgoing
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_template is not None:
            result['cardTemplate'] = self.card_template

        if self.daily_noc is not None:
            result['dailyNoc'] = self.daily_noc

        if self.daily_noc_time is not None:
            result['dailyNocTime'] = self.daily_noc_time

        if self.ding_sign_key is not None:
            result['dingSignKey'] = self.ding_sign_key

        if self.enable_outgoing is not None:
            result['enableOutgoing'] = self.enable_outgoing

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardTemplate') is not None:
            self.card_template = m.get('cardTemplate')

        if m.get('dailyNoc') is not None:
            self.daily_noc = m.get('dailyNoc')

        if m.get('dailyNocTime') is not None:
            self.daily_noc_time = m.get('dailyNocTime')

        if m.get('dingSignKey') is not None:
            self.ding_sign_key = m.get('dingSignKey')

        if m.get('enableOutgoing') is not None:
            self.enable_outgoing = m.get('enableOutgoing')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

