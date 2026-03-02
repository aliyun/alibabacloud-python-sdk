# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Log4jLogger(DaraModel):
    def __init__(
        self,
        logger_level: str = None,
        logger_name: str = None,
    ):
        # The level of the output log.
        self.logger_level = logger_level
        # The name of the class of the output log.
        self.logger_name = logger_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logger_level is not None:
            result['loggerLevel'] = self.logger_level

        if self.logger_name is not None:
            result['loggerName'] = self.logger_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loggerLevel') is not None:
            self.logger_level = m.get('loggerLevel')

        if m.get('loggerName') is not None:
            self.logger_name = m.get('loggerName')

        return self

