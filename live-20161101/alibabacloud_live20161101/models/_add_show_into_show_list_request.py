# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class AddShowIntoShowListRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        duration: int = None,
        live_input_type: int = None,
        owner_id: int = None,
        region_id: str = None,
        repeat_times: int = None,
        resource_id: str = None,
        resource_type: str = None,
        resource_url: str = None,
        show_name: str = None,
        spot: int = None,
        is_batch_mode: bool = None,
        show_list: List[main_models.AddShowIntoShowListRequestShowList] = None,
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
        # The duration of the episode. Unit: seconds.
        # 
        # > You can specify only one of the **RepeatTimes** and **Duration** parameters.
        self.duration = duration
        # The custom type label.
        self.live_input_type = live_input_type
        self.owner_id = owner_id
        self.region_id = region_id
        # The number of times the episode repeats after the first playback is complete. The default value is 0.
        # 
        # > 
        # 
        # *   You can specify only one of the **RepeatTimes** and **Duration** parameters. - The RepeatTimes parameter specifies the number of repetitions. For example, if you set the value to -1, the episode is to be played for infinite times. If you set the value to 0, the episode is to be played once. If you set the value to 1, the episode is to be played twice.
        self.repeat_times = repeat_times
        # The ID of the resource.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   live: live stream
        # *   vod: on-demand video
        # *   pic: image
        # 
        # > 
        # 
        # *   When you select media resources from ApsaraVideo VOD, we recommend that you select resources that are stored in hosted OSS buckets. Resources stored in non-hosted OSS buckets have a validity period. Pay attention to the validity if you select resources that are stored in non-hosted OSS buckets. - You can add a live stream from ApsaraVideo Live or by using a third-party URL. - You can add an on-demand video from ApsaraVideo VOD or by using a third-party URL, or add an on-demand image.
        self.resource_type = resource_type
        # The URL of the resource.
        self.resource_url = resource_url
        # The name of the episode.
        self.show_name = show_name
        # The position of the episode in the episode list. Position indexes start from 0. By default, the episode is added to the end of the episode list.
        self.spot = spot
        # Specifies whether to add multiple episodes to the episode list at a time. Valid values:
        # 
        # *   true: adds multiple episodes to the episode list at a time.
        # *   false: adds a single episode to the episode list.
        # 
        # > If you do not specify this parameter or this parameter is left empty, a single episode is to be added to the episode list.
        self.is_batch_mode = is_batch_mode
        # The episodes that you want to add to the episode list. Each episode has a unique name and resource URL.
        self.show_list = show_list

    def validate(self):
        if self.show_list:
            for v1 in self.show_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.live_input_type is not None:
            result['LiveInputType'] = self.live_input_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_url is not None:
            result['ResourceUrl'] = self.resource_url

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.spot is not None:
            result['Spot'] = self.spot

        if self.is_batch_mode is not None:
            result['isBatchMode'] = self.is_batch_mode

        result['showList'] = []
        if self.show_list is not None:
            for k1 in self.show_list:
                result['showList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('LiveInputType') is not None:
            self.live_input_type = m.get('LiveInputType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceUrl') is not None:
            self.resource_url = m.get('ResourceUrl')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Spot') is not None:
            self.spot = m.get('Spot')

        if m.get('isBatchMode') is not None:
            self.is_batch_mode = m.get('isBatchMode')

        self.show_list = []
        if m.get('showList') is not None:
            for k1 in m.get('showList'):
                temp_model = main_models.AddShowIntoShowListRequestShowList()
                self.show_list.append(temp_model.from_map(k1))

        return self

class AddShowIntoShowListRequestShowList(DaraModel):
    def __init__(
        self,
        duration: int = None,
        live_input_type: int = None,
        repeat_times: int = None,
        resource_id: str = None,
        resource_type: str = None,
        resource_url: str = None,
        show_name: str = None,
    ):
        # The duration of the episode. Unit: seconds.
        # 
        # >  You can specify only one of the **RepeatTimes** and **Duration** parameters.
        self.duration = duration
        # The custom type label.
        self.live_input_type = live_input_type
        # The number of times the episode repeats after the first playback is complete. Default value: 0.
        # 
        # > 
        # 
        # *   You can specify only one of the **RepeatTimes** and **Duration** parameters.
        # 
        # *   The RepeatTimes parameter specifies the number of repetitions. For example, if you set the value to 0, the episode is to be played once. If you set the value to 1, the episode is to be played twice.
        self.repeat_times = repeat_times
        # The ID of the resource.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   live: live stream
        # *   vod: on-demand video
        # *   pic: image
        # 
        # > 
        # 
        # *   When you select media resources from ApsaraVideo VOD, we recommend that you select resources that are stored in hosted OSS buckets. Resources stored in non-hosted OSS buckets have a validity period. Pay attention to the validity if you select resources that are stored in non-hosted OSS buckets.
        # 
        # *   You can add a live stream from ApsaraVideo Live or by using a third-party URL.
        # *   You can add an on-demand video from ApsaraVideo VOD or by using a third-party URL, or add an on-demand image.
        self.resource_type = resource_type
        # The URL of the resource.
        self.resource_url = resource_url
        # The name of the episode.
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.live_input_type is not None:
            result['liveInputType'] = self.live_input_type

        if self.repeat_times is not None:
            result['repeatTimes'] = self.repeat_times

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.resource_url is not None:
            result['resourceUrl'] = self.resource_url

        if self.show_name is not None:
            result['showName'] = self.show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('liveInputType') is not None:
            self.live_input_type = m.get('liveInputType')

        if m.get('repeatTimes') is not None:
            self.repeat_times = m.get('repeatTimes')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('resourceUrl') is not None:
            self.resource_url = m.get('resourceUrl')

        if m.get('showName') is not None:
            self.show_name = m.get('showName')

        return self

