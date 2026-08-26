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
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value returned in the response.
        # 
        # - If you created the production studio in the LIVE console, find the production studio name on the Cloud Production Studio page. To go to the page, choose **LIVE Console** > **Production Studio** > **Cloud Production Studio**.
        # 
        # > The name of the production studio on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The highest-priority show.
        # 
        # > This parameter can be configured only before the playlist starts.
        self.high_priority_show_id = high_priority_show_id
        # The time to play the highest-priority show. The format is yyyy-MM-dd\\"T\\"HH:mm:ss.
        # 
        # > This parameter can be configured only before the playlist starts.<br>
        # > After this parameter is configured, the system switches from the currently playing show to the highest-priority show at the specified time.
        self.high_priority_show_start_time = high_priority_show_start_time
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The number of times the playlist loops.
        # 
        # > - RepeatTimes specifies the number of repetitions. For example, a value of **0** means the playlist is played once without repetition. A value of **1** means the playlist is played twice (one initial playback and one repetition).
        # >
        # > - A value of -1 indicates that the playlist loops indefinitely.
        self.repeat_times = repeat_times
        # The ID of the show whose position in the playlist you want to modify.
        # 
        # > Obtain the ShowId value from the response of the [AddShowIntoShowList](https://help.aliyun.com/document_detail/2848051.html) or [DescribeShowList](https://help.aliyun.com/document_detail/2848054.html) operation.
        self.show_id = show_id
        # The new position of the show in the playlist. The show specified by ShowId is moved to the position specified by **Spot**.
        # 
        # > The value must be greater than or equal to 0 and less than or equal to the total number of shows in the playlist.
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

