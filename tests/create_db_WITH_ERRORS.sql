CREATE TABLE IF NOT EXISTS softpaq_lookup (
    softpaq_id INTEGER NOT NULL,
    os_version TEXT NOT NULL,
    downloading INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (softpaq_id),
    CHECK(downloading = 0 OR downloading = 1)
) STRICT  -- ERROR: No semicolon

CREATE TABLE IF NOT EXISTS softpaq_info (
    softpaq_id INTEGER NOT NULL  -- ERROR: No comma
    softpaq_path TEXT NOT NULL,
    download_datetime TEXT NOT NULL,
    update_datetime TEXT,
    uri TEXT NOT NULL,
    FOREIGN KEY (softpaq_id)
        REFERENCES softpaq_lookup (softpaq_id)
        ON DELETE CASCADE
) STRICT;

CREATE TABLE IF NOT EXISTS machine_lookup (
    machine_id TEXT NOT NULL,
    machine_name TEXT NOT NULL,
    softpaq_id INTEGER NOT NULL,
    PRIMARY KEY (machine_id),
    FOREIGN KEY (softpaq_id  -- ERROR: No closing paranthesis
        REFERENCES softpaq_lookup (softpaq_id),
    CHECK (length(machine_id) = 4)
) STRICT;