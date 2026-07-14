# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SeverityNotifyConfig(DaraModel):
    def __init__(
        self,
        receivers: List[main_models.DirectNotifyReceiver] = None,
        send_recover_notification: bool = None,
    ):
        self.receivers = receivers
        self.send_recover_notification = send_recover_notification

    def validate(self):
        if self.receivers:
            for v1 in self.receivers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['receivers'] = []
        if self.receivers is not None:
            for k1 in self.receivers:
                result['receivers'].append(k1.to_map() if k1 else None)

        if self.send_recover_notification is not None:
            result['sendRecoverNotification'] = self.send_recover_notification

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.receivers = []
        if m.get('receivers') is not None:
            for k1 in m.get('receivers'):
                temp_model = main_models.DirectNotifyReceiver()
                self.receivers.append(temp_model.from_map(k1))

        if m.get('sendRecoverNotification') is not None:
            self.send_recover_notification = m.get('sendRecoverNotification')

        return self

