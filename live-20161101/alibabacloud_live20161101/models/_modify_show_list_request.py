# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyShowListRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        high_priority_show_id: str = None,
        high_priority_show_start_time: str = None,
        owner_id: int = None,
        region_id: str = None,
        repeat_times: int = None,
        show_id: str = None,
        spot: int = None,
    ):
        # The ID of the production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The episode of the highest priority.
        # 
        # >  You can configure this parameter only before the playback of the episode list starts.
        self.high_priority_show_id = high_priority_show_id
        # The time at which the episode of the highest priority is played. Format: yyyy-MM-dd\\"T\\"HH:mm:ss.
        # 
        # >  You can configure this parameter only before the episode list starts playing.\\
        # After you configure this parameter, when the specified point in time is reached, any episode that is playing stops and the episode of the highest priority in the episode list starts to play.
        self.high_priority_show_start_time = high_priority_show_start_time
        self.owner_id = owner_id
        self.region_id = region_id
        # The number of additional times the episode list is played.
        # 
        # > 
        # 
        # *   The RepeatTimes parameter specifies the number of repetitions. For example, if you set the value to **0**, the episode list is played **once**. If you set the value to **1**, the episode list is played **twice**.********
        # 
        # *   If you set the value to -1, the episode list is repeated indefinitely.
        self.repeat_times = repeat_times
        # The ID of the episode for which you want to change the position in the playlist.
        # 
        # >  You can call the [AddShowIntoShowList](https://help.aliyun.com/document_detail/2848051.html) or [DescribeShowList](https://help.aliyun.com/document_detail/2848054.html) operation and check the value of the response parameter ShowId to obtain the ID.
        self.show_id = show_id
        # The position of the episode in the episode list. If you want to change the position of an episode in a playlist, place the ID of the episode in **Spot**.
        # 
        # >  The value must be greater than or equal to 0 and less than or equal to the total number of episodes in the playlist.
        self.spot = spot

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.high_priority_show_id is not None:
            result['HighPriorityShowId'] = self.high_priority_show_id

        if self.high_priority_show_start_time is not None:
            result['HighPriorityShowStartTime'] = self.high_priority_show_start_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times

        if self.show_id is not None:
            result['ShowId'] = self.show_id

        if self.spot is not None:
            result['Spot'] = self.spot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('HighPriorityShowId') is not None:
            self.high_priority_show_id = m.get('HighPriorityShowId')

        if m.get('HighPriorityShowStartTime') is not None:
            self.high_priority_show_start_time = m.get('HighPriorityShowStartTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')

        if m.get('ShowId') is not None:
            self.show_id = m.get('ShowId')

        if m.get('Spot') is not None:
            self.spot = m.get('Spot')

        return self

