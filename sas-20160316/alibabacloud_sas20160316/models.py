# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class IsSasServiceOpeningRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class IsSasServiceOpeningResponse(TeaModel):
    def __init__(self, data=None, code=None, message=None, success=None):
        self.data = data                # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['data'] = self.data
        result['code'] = self.code
        result['message'] = self.message
        result['success'] = self.success
        return result

    def from_map(self, map={}):
        self.data = map.get('data')
        self.code = map.get('code')
        self.message = map.get('message')
        self.success = map.get('success')
        return self


class GetEventsCountRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetEventsCountResponse(TeaModel):
    def __init__(self, code=None, message=None, success=None, event_count=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.event_count = event_count  # type: GetEventsCountResponseEventCount

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.event_count, 'event_count')
        if self.event_count:
            self.event_count.validate()

    def to_map(self):
        result = {}
        result['code'] = self.code
        result['message'] = self.message
        result['success'] = self.success
        if self.event_count is not None:
            result['EventCount'] = self.event_count.to_map()
        else:
            result['EventCount'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.message = map.get('message')
        self.success = map.get('success')
        if map.get('EventCount') is not None:
            temp_model = GetEventsCountResponseEventCount()
            self.event_count = temp_model.from_map(map['EventCount'])
        else:
            self.event_count = None
        return self


class GetEventsCountResponseEventCount(TeaModel):
    def __init__(self, event=None, attack=None, vul=None):
        self.event = event              # type: int
        self.attack = attack            # type: int
        self.vul = vul                  # type: int

    def validate(self):
        self.validate_required(self.event, 'event')
        self.validate_required(self.attack, 'attack')
        self.validate_required(self.vul, 'vul')

    def to_map(self):
        result = {}
        result['event'] = self.event
        result['attack'] = self.attack
        result['vul'] = self.vul
        return result

    def from_map(self, map={}):
        self.event = map.get('event')
        self.attack = map.get('attack')
        self.vul = map.get('vul')
        return self


