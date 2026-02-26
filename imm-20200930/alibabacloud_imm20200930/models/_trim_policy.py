# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrimPolicy(DaraModel):
    def __init__(
        self,
        disable_delete_empty_cell: bool = None,
        disable_delete_repeated_style: bool = None,
        disable_delete_unused_picture: bool = None,
        disable_delete_unused_shape: bool = None,
    ):
        # Specifies whether to prevent all empty cells from being deleted. Valid values:
        # 
        # *   true
        # *   false
        self.disable_delete_empty_cell = disable_delete_empty_cell
        # Specifies whether to prevent all duplicate styles from being deleted. Valid values:
        # 
        # *   true
        # *   false
        self.disable_delete_repeated_style = disable_delete_repeated_style
        # Specifies whether to prevent unused cell images from being deleted. Valid values:
        # 
        # *   true
        # *   false
        self.disable_delete_unused_picture = disable_delete_unused_picture
        # Specifies whether to prevent unused shapes from being deleted. Valid values:
        # 
        # *   true
        # *   false
        self.disable_delete_unused_shape = disable_delete_unused_shape

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_delete_empty_cell is not None:
            result['DisableDeleteEmptyCell'] = self.disable_delete_empty_cell

        if self.disable_delete_repeated_style is not None:
            result['DisableDeleteRepeatedStyle'] = self.disable_delete_repeated_style

        if self.disable_delete_unused_picture is not None:
            result['DisableDeleteUnusedPicture'] = self.disable_delete_unused_picture

        if self.disable_delete_unused_shape is not None:
            result['DisableDeleteUnusedShape'] = self.disable_delete_unused_shape

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableDeleteEmptyCell') is not None:
            self.disable_delete_empty_cell = m.get('DisableDeleteEmptyCell')

        if m.get('DisableDeleteRepeatedStyle') is not None:
            self.disable_delete_repeated_style = m.get('DisableDeleteRepeatedStyle')

        if m.get('DisableDeleteUnusedPicture') is not None:
            self.disable_delete_unused_picture = m.get('DisableDeleteUnusedPicture')

        if m.get('DisableDeleteUnusedShape') is not None:
            self.disable_delete_unused_shape = m.get('DisableDeleteUnusedShape')

        return self

