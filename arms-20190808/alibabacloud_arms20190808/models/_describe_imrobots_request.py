# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIMRobotsRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        robot_ids: str = None,
        robot_name: str = None,
        size: int = None,
    ):
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # The chatbot IDs.
        self.robot_ids = robot_ids
        # The name of the IM chatbot.
        self.robot_name = robot_name
        # The number of IM chatbots to return on each page.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.robot_ids is not None:
            result['RobotIds'] = self.robot_ids

        if self.robot_name is not None:
            result['RobotName'] = self.robot_name

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('RobotIds') is not None:
            self.robot_ids = m.get('RobotIds')

        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

