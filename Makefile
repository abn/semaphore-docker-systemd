
SERVICE_DIR := /usr/lib/systemd/system
LIB_DIR := /var/lib/semaphore

.PHONY: all install

all: install

$(LIB_DIR):
	@mkdir -p $(LIB_DIR)

$(LIB_DIR)/mongo: $(LIB_DIR)
	@mkdir -p $(LIB_DIR)/mongo

install: $(LIB_DIR)/mongo $(SERVICE_DIR)
	@mkdir -p $(LIB_DIR)/mongo
	@chcon -Rt svirt_sandbox_file_T $(LIB_DIR)/mongo
	@cp -$ semaphore*.service $(SERVICE_DIR)/.
