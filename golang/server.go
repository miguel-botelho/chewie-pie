package main

import (
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		body, err := ioutil.ReadAll(r.Body)
		if err != nil {
			log.Fatal(err)
		}
		log.Println(string(body))

		w.WriteHeader(200)
		w.Write([]byte(`These are not the droids you're looking for`))
	})

	http.ListenAndServe(":5000", nil)
}
