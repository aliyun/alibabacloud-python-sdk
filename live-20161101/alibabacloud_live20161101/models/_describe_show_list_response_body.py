# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeShowListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        show_list: str = None,
        show_list_info: main_models.DescribeShowListResponseBodyShowListInfo = None,
    ):
        # The request ID.
        self.request_id = request_id
        # ****Details of the episode list.
        # 
        # Show indicates the information about a specific episode. For more information, see the **Show** parameter.
        self.show_list = show_list
        # The information about the episode list.
        self.show_list_info = show_list_info

    def validate(self):
        if self.show_list_info:
            self.show_list_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_list is not None:
            result['ShowList'] = self.show_list

        if self.show_list_info is not None:
            result['ShowListInfo'] = self.show_list_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowList') is not None:
            self.show_list = m.get('ShowList')

        if m.get('ShowListInfo') is not None:
            temp_model = main_models.DescribeShowListResponseBodyShowListInfo()
            self.show_list_info = temp_model.from_map(m.get('ShowListInfo'))

        return self

class DescribeShowListResponseBodyShowListInfo(DaraModel):
    def __init__(
        self,
        background: str = None,
        current_show_id: str = None,
        high_priority_show_id: str = None,
        high_priority_show_start_time: str = None,
        show_list: main_models.DescribeShowListResponseBodyShowListInfoShowList = None,
        show_list_repeat_times: int = None,
        total_show_list_repeat_times: int = None,
    ):
        # The background of the episode list.
        self.background = background
        # The ID of the episode that is playing.
        self.current_show_id = current_show_id
        # The episode of the highest priority.
        # 
        # > You can configure this parameter only before the episode list starts playing.
        self.high_priority_show_id = high_priority_show_id
        # The time at which the episode of the highest priority is played. Format: yyyy-MM-dd\\"T\\"HH:mm:ss.
        # 
        # > You can configure this parameter only before the episode list starts playing. After you configure this parameter, when the specified point in time is reached, any episode that is playing stops and the episode of the highest priority in the episode list starts to play.
        self.high_priority_show_start_time = high_priority_show_start_time
        # The episodes in the episode list.
        self.show_list = show_list
        # The number of additional times the episode list is played by default. The value is 0.
        self.show_list_repeat_times = show_list_repeat_times
        # The number of additional times the episode list is played.
        self.total_show_list_repeat_times = total_show_list_repeat_times

    def validate(self):
        if self.show_list:
            self.show_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background is not None:
            result['Background'] = self.background

        if self.current_show_id is not None:
            result['CurrentShowId'] = self.current_show_id

        if self.high_priority_show_id is not None:
            result['HighPriorityShowId'] = self.high_priority_show_id

        if self.high_priority_show_start_time is not None:
            result['HighPriorityShowStartTime'] = self.high_priority_show_start_time

        if self.show_list is not None:
            result['ShowList'] = self.show_list.to_map()

        if self.show_list_repeat_times is not None:
            result['ShowListRepeatTimes'] = self.show_list_repeat_times

        if self.total_show_list_repeat_times is not None:
            result['TotalShowListRepeatTimes'] = self.total_show_list_repeat_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Background') is not None:
            self.background = m.get('Background')

        if m.get('CurrentShowId') is not None:
            self.current_show_id = m.get('CurrentShowId')

        if m.get('HighPriorityShowId') is not None:
            self.high_priority_show_id = m.get('HighPriorityShowId')

        if m.get('HighPriorityShowStartTime') is not None:
            self.high_priority_show_start_time = m.get('HighPriorityShowStartTime')

        if m.get('ShowList') is not None:
            temp_model = main_models.DescribeShowListResponseBodyShowListInfoShowList()
            self.show_list = temp_model.from_map(m.get('ShowList'))

        if m.get('ShowListRepeatTimes') is not None:
            self.show_list_repeat_times = m.get('ShowListRepeatTimes')

        if m.get('TotalShowListRepeatTimes') is not None:
            self.total_show_list_repeat_times = m.get('TotalShowListRepeatTimes')

        return self

class DescribeShowListResponseBodyShowListInfoShowList(DaraModel):
    def __init__(
        self,
        show: List[main_models.DescribeShowListResponseBodyShowListInfoShowListShow] = None,
    ):
        self.show = show

    def validate(self):
        if self.show:
            for v1 in self.show:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Show'] = []
        if self.show is not None:
            for k1 in self.show:
                result['Show'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.show = []
        if m.get('Show') is not None:
            for k1 in m.get('Show'):
                temp_model = main_models.DescribeShowListResponseBodyShowListInfoShowListShow()
                self.show.append(temp_model.from_map(k1))

        return self

class DescribeShowListResponseBodyShowListInfoShowListShow(DaraModel):
    def __init__(
        self,
        duration: int = None,
        repeat_times: int = None,
        resource_info: main_models.DescribeShowListResponseBodyShowListInfoShowListShowResourceInfo = None,
        show_id: str = None,
        show_name: str = None,
    ):
        # The duration of the episode. Unit: seconds.
        self.duration = duration
        # The number of times the episode repeats after the first playback is complete.
        # 
        # For example, if you set the value to 0, the episode is to be played once. If you set the value to 1, the episode is to be played twice.
        self.repeat_times = repeat_times
        # The resource information.
        self.resource_info = resource_info
        # The ID of the episode.
        self.show_id = show_id
        # The name of the episode.
        self.show_name = show_name

    def validate(self):
        if self.resource_info:
            self.resource_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times

        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info.to_map()

        if self.show_id is not None:
            result['ShowId'] = self.show_id

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')

        if m.get('ResourceInfo') is not None:
            temp_model = main_models.DescribeShowListResponseBodyShowListInfoShowListShowResourceInfo()
            self.resource_info = temp_model.from_map(m.get('ResourceInfo'))

        if m.get('ShowId') is not None:
            self.show_id = m.get('ShowId')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        return self

class DescribeShowListResponseBodyShowListInfoShowListShowResourceInfo(DaraModel):
    def __init__(
        self,
        live_input_type: int = None,
        resource_id: str = None,
        resource_type: str = None,
        resource_url: str = None,
    ):
        # The custom type label.
        self.live_input_type = live_input_type
        # The ID of the video-on-demand (VOD) file.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The URL of the resource.
        self.resource_url = resource_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_input_type is not None:
            result['LiveInputType'] = self.live_input_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_url is not None:
            result['ResourceUrl'] = self.resource_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveInputType') is not None:
            self.live_input_type = m.get('LiveInputType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceUrl') is not None:
            self.resource_url = m.get('ResourceUrl')

        return self

