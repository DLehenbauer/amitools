from BlockDevice import BlockDevice
import os.path
import os

from ImageFile import ImageFile

class RawBlockDevice(BlockDevice):
  def __init__(self, raw_file, read_only=False, block_bytes=512):
    self.img_file = ImageFile(raw_file, read_only, block_bytes)

  def create(self, num_blocks):
    self.img_file.create(num_blocks)
    self.open()

  def open(self):
    self.img_file.open()
    # calc block longs
    self.block_bytes = self.img_file.block_bytes
    self.block_longs = self.block_bytes / 4
          
  def flush(self):
    pass
        
  def close(self):
    self.img_file.close()

  def read_block(self, blk_num):
    return self.img_file.read_blk(blk_num)
  
  def write_block(self, blk_num, data):
    self.img_file.write_blk(blk_num, data)
