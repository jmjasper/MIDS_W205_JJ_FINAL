(ns tweetsent
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetsent [options]
   [
    ;; spout configuration
    {"Tweet-spout" (python-spout-spec
          options
          "spouts.Tweets.Tweets"
          ["tweet"]
          )
    }
    ;; bolt configuration
{"Db-bolt" (python-bolt-spec
          options
          {"Tweet-spout" :shuffle}
          "bolts.Db.Db"
          ["word"]
          :p 2
          )

;; bolt configuration -- 2
"Rt-bolt" (python-bolt-spec
          options
          {"Tweet-spout" :shuffle}
          "bolts.Rt.Rt"
          ;;Just for testing -- eventually will be savable
          ["word" "sentiment"]
          :p 2
          )
    }

  ]
)
