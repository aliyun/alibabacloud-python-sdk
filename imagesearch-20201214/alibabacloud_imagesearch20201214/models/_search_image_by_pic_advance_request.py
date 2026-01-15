# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class SearchImageByPicAdvanceRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        distinct_product_id: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        pic_content_object: BinaryIO = None,
        region: str = None,
        score_threshold: str = None,
        start: int = None,
    ):
        # The category of the product. For more information, see [Category references](https://help.aliyun.com/document_detail/179184.html).
        # 
        # *   For product search: If a category is specified, the specified category prevails. If no category is specified, the system estimates and selects a category. The category selected by the system is included in the response.
        # *   For generic search: The parameter value is set to 88888888 regardless of whether a category is specified.
        self.category_id = category_id
        # Specifies whether to recognize the subject in the image and search for images based on the recognized subject. Valid values: true and false. Default value: true.
        # 
        # *   true: The system recognizes the subject in the image, and searches for images based on the recognized subject. The recognition result is included in the response.
        # *   false: The system does not recognize the subject of the image, and searches for images based on the entire image.
        self.crop = crop
        self.distinct_product_id = distinct_product_id
        # The filter conditions. int_attr supports the following operators: >, >=, <, <=, and =. str_attr supports the following operators: = and !=. You can set the logical operator between conditions to AND or OR.
        # 
        # Examples:
        # 
        # *   int_attr>=100
        # *   str_attr!="value1"
        # *   Example: int_attr=1000 AND str_attr="value1"
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of images to return on each page. Valid values: 1 to 100. Default value: 10.
        self.num = num
        # The image file. The image file is encoded in Base64.
        # 
        # *   The file size of the image cannot exceed 4 MB.
        # *   The following image formats are supported: PNG, JPG, JPEG, BMP, GIF, WebP, TIFF, and PPM.
        # *   The transmission timeout period cannot exceed 5 seconds.
        # *   For brand image searches, the length and the width of the image must range from 200 pixels to 4,096 pixels.
        # *   For cloth image searches, the length and the width of the image must range from 448 pixels to 4,096 pixels.
        # *   For product and generic image searches, the length and the width of the image must range from 100 pixels to 4,096 pixels.
        # *   The image cannot contain rotation settings.
        # 
        # This parameter is required.
        self.pic_content_object = pic_content_object
        # The subject area of the image. Specify the subject area in the following format: `x1,x2,y1,y2`. `x1 and y1` represent the upper-left corner pixel. `x2 and y2` represent the lower-right corner pixel.
        # 
        # >*   If you set the Region parameter, the system searches for images based on the value of Region regardless of the value of the Crop parameter.
        self.region = region
        self.score_threshold = score_threshold
        # The number of the image to return. Valid values: 0 to 499. Default value: 0.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.distinct_product_id is not None:
            result['DistinctProductId'] = self.distinct_product_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.num is not None:
            result['Num'] = self.num

        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object

        if self.region is not None:
            result['Region'] = self.region

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('DistinctProductId') is not None:
            self.distinct_product_id = m.get('DistinctProductId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

